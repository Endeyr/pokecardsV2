from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class AdvSearchView(LoginRequiredMixin, generic.TemplateView):
    """
    TemplateView used for our advanced serach page

    **Template:**

    :template:'core/adv-search.html'
    """

    template_name = "core/adv-search.html"
    login_url = "users:login"
