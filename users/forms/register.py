from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"


class RegisterForm(UserCreationForm):
    """
    Form that uses built-in UserCreationForm to handle user creation
    """

    username = forms.CharField(
        label="Username",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "*Your username...", "class": INPUT_CLASSES}
        ),
    )
    email = forms.EmailField(
        label="Email",
        max_length=254,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "*Email...", "class": INPUT_CLASSES}
        ),
    )
    first_name = forms.CharField(
        label="First Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "*Your first name...", "class": INPUT_CLASSES}
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "*Your last name...", "class": INPUT_CLASSES}
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "*Password...", "class": INPUT_CLASSES}
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "*Confirm Password...", "class": INPUT_CLASSES}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
