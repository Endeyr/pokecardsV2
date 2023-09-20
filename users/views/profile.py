from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from users.models.profile import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, generic.DetailView):
    """
    DetailView used for our profile page
    """

    model = Profile
    template_name = "users/profile.html"
    login_url = "users:login"
