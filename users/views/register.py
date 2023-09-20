from django.views import generic
from django.urls import reverse_lazy
from users.forms import RegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin


class RegisterView(
    UserPassesTestMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """
    CreateView used for our register page
    """

    template_name = "registration/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("core:home")
    success_message = "Account created!"
    permission_denied_message = "You are already registered!"

    def test_func(self):
        return self.request.user.is_anonymous

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
