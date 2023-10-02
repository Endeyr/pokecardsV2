from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from users.forms import UpdatePasswordResetForm
import os


class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    template_name = "registration/password_reset_form.html"
    success_message = "Success"
    success_url = reverse_lazy("users:password_reset_done")
    form_class = UpdatePasswordResetForm
    from_email = os.getenv("DEFAULT_FROM_EMAIL")
