from django.views import generic
from users.forms import UpdateProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from users.models.profile import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateProfileView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    UpdateView used for our profile update page
    """

    template_name = "users/update-profile.html"
    context_object_name = "user"
    model = Profile
    form_class = UpdateProfileForm
    success_message = "Profile updated!"
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def get_success_url(self):
        return reverse_lazy("users:profile", kwargs={"pk": self.object.pk})

    def get_initial(self):
        user = self.request.user
        context = {
            "bio": user.profile.bio,
            "avatar": user.profile.avatar,
        }
        return context
