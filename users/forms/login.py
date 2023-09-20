from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    """
    Form that uses built-in AuthenticationForm to handle user creation
    """

    INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"

    username = forms.CharField(
        label="Username",
        max_length=254,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "*Username...", "class": INPUT_CLASSES}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "*Password...", "class": INPUT_CLASSES}
        ),
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = self.INPUT_CLASSES

    class Meta:
        model = User
        fields = ("username", "password")
