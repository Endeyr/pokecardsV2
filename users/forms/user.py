from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"


class UpdateUserForm(UserChangeForm):
    """
    Update the user information
    """

    password = None

    username = forms.CharField(
        label="Username",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "*Username...", "class": INPUT_CLASSES}
        ),
    )

    first_name = forms.CharField(
        label="First Name",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "*First Name...", "class": INPUT_CLASSES}
        ),
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "*Last Name...", "class": INPUT_CLASSES}
        ),
    )

    email = forms.EmailField(
        label="Email",
        max_length=255,
        required=False,
        widget=forms.EmailInput(
            attrs={"placeholder": "*Email...", "class": INPUT_CLASSES}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
