from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class SearchView(LoginRequiredMixin, generic.TemplateView):
    """
    FormView used for our search page.
    """

    template_name = "core/search.html"
    login_url = "users:login"
