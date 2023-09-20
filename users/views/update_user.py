from django.views import generic
from users.forms import UpdateUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    """
    UpdateView used for our user update page
    """

    template_name = "users/update-user.html"
    form_class = UpdateUserForm
    context_object_name = "user"
    model = User
    success_message = "User updated!"
    login_url = "users:login"

    def get_success_url(self):
        return reverse_lazy("users:profile", kwargs={"pk": self.object.pk})

    def get_initial(self):
        user = self.request.user
        context = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
        return context
