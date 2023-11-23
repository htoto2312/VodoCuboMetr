from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

#
#
urlpatterns = [
     path("", IndexView.as_view(), name="home"),
     path("signup/", UserCreateView.as_view(), name="signup"),
     path("login/", MyLoginView.as_view(), name="login"),
     path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
     path("water/", WaterCreateView.as_view(), name="water"),
     path('pay/<int:pk>/', PayView.as_view(), name='pay'),
     path('pay_all/', PayAllView.as_view(), name='pay_all'),
     path('profile/',  ProfileView.as_view(), name='profile'),
#     path("add_note/", CreateNoteView.as_view(), name="add_note"),
#     path("delete_note/<int:note_id>", DeleteNoteView.as_view(), name="delete_note"),
#     path("mark_note/", CheckedView.as_view(), name="check_note"),
#     path("messages/", test_messages, name="messages"),
#     path("session/", get_session),
 ]
