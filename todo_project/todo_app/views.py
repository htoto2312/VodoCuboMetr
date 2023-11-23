from typing import Any
import json

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from .forms import UserCreateForm, LoginUserForm, WaterForm
from .models import MyUser, Water
from django.shortcuts import render
from .models import Water
from .forms import WaterForm
from django.utils import timezone
from datetime import timedelta

# from .models import Note
#
class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'todo_app/profile.html', {'user': request.user})

class MyLoginView(LoginView):
     template_name = "todo_app/login.html"
     redirect_authenticated_user = True
     form_class = LoginUserForm
#
     def get_success_url(self) -> str:
         return reverse_lazy("home")

# # Create your views here.
class IndexView( TemplateView): #LoginRequiredMixin
    template_name = "todo_app/index.html"
#
#




class UserCreateView(CreateView):

    template_name = "todo_app/signup.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("home")
    required = False




class WaterCreateView(LoginRequiredMixin,CreateView):

    model = Water
    form_class = WaterForm
    template_name = 'todo_app/water.html'
    success_url = reverse_lazy("water")
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        waters  = Water.objects.filter(author=self.request.user).order_by('-id')
        context['waters'] = waters
        context['unpaid_exists'] = waters.filter(is_paid=False).exists()
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        last_water = Water.objects.filter(author=self.request.user).order_by('-id').first()
        if last_water and last_water.created_at > timezone.now() - timedelta(days=30):
            form.add_error(None, 'Ви можете добавляти данні лише один раз на місяць')
            return self.form_invalid(form)
        return super().form_valid(form)

class PayView(View):
    def get(self, request, *args, **kwargs):
        water = Water.objects.get(id=kwargs['pk'])
        water.is_paid = True
        water.save()
        return redirect('water')

class PayAllView(View):
    def get(self, request, *args, **kwargs):
        waters = Water.objects.filter(author=request.user, is_paid=False)
        waters.update(is_paid=True)
        return redirect('water')
# class WaterListView(LoginRequiredMixin, ListView):
#
#     template_name = "todo_app/water.html"
#     model = MyUser
#     context_object_name = "notes"
#
#     def get_queryset(self) -> QuerySet[Any]:
#         return self.model.objects.filter(author=self.request.user).all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = WaterForm()
#         return context

# class UserCreateView(CreateView):
#     def register(request):
#         if request.method == 'POST':
#             user_form = UserCreateForm(request.POST)
#             if user_form.is_valid():
#
#
#             # Create a new user object but avoid saving it yet
#                 new_user = user_form.save(commit=False)
#             # Set the chosen password
#
#
#                 new_user.set_password(user_form.cleaned_data['password'])
#             # Save the User object
#
#
#                 new_user.save()
#                 return render(request, 'account/register_done.html', {'new_user': new_user})
#         else:
#             user_form = UserCreateForm()
#         return render(request, 'signup.html', {'user_form': user_form})
#
#
# class NotesListView(LoginRequiredMixin, ListView):
#     paginate_by = 3
#     template_name = "todo_app/water.html"
#     model = Note
#     context_object_name = "notes"
#
#     def get_queryset(self) -> QuerySet[Any]:
#         return self.model.objects.filter(author=self.request.user).all()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = NoteForm()
#         return context
#
#
# class CreateNoteView(CreateView):
#     template_name = "todo_app/water.html"
#     form_class = NoteForm
#     success_url = reverse_lazy("notes")
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class DeleteNoteView(DeleteView):
#     template_name = "todo_app/water.html"
#     success_url = reverse_lazy("notes")
#     model = Note
#     pk_url_kwarg = "note_id"
#
#
# @method_decorator(csrf_exempt, name="dispatch")
# class CheckedView(View):
#     def post(self, request, *args, **kwargs):
#         data = json.loads(self.request.body)
#         note_id = data.get("note_id")
#         is_checked = data.get("checked")
#         try:
#             note = Note.objects.get(id=note_id)
#         except Note.DoesNotExist:
#             return JsonResponse({"error": "Note does not exist"})
#         if note.author.id is not self.request.user.id:
#             return JsonResponse({"error": "Authentication credentials were missed"})
#         note.finished = is_checked
#         note.save()
#         return JsonResponse({"message": "OK"})
#
#
# def test_messages(request: HttpRequest):
#     # DEBUG INFO SUCCESS WARNING ERROR
#     request.session["testvar"] = "TestString"
#     messages.info(request, message=" ")
#     messages.warning(request, message="з ", extra_tags="qwer")
#     return render(request=request, template_name="todo_app/messages.html")
#
#
# def get_session(request: HttpRequest):
#     print(dict(request.session))
#     return HttpResponse(".")
