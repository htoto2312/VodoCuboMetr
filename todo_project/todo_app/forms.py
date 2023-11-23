from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Water, MyUser


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ['cubometrs']


class UserCreateForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username",  'first_name', "last_name", "email")
        widgets = {"password": forms.PasswordInput}

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "id": "inputUsername", "class": "input"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "input", "id": "inputPw"}
        )
    )

