from django.contrib.auth.views import LoginView
from users.forms.login import LoginForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    form_class = LoginForm
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("core:home")
