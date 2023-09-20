from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from users.forms import UpdatePasswordChangeForm


class CustomPasswordChangeView(
    LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView
):
    template_name = "registration/password_change_form.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("core:home")
    login_url = "users:login"
    form_class = UpdatePasswordChangeForm
