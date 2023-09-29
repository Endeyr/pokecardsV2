from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Collection


class SearchView(LoginRequiredMixin, generic.TemplateView):
    """
    FormView used for our search page.
    """

    template_name = "core/search.html"
    login_url = "users:login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["collections"] = Collection.objects.filter(user=user)
        return context
