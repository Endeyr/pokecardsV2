from django.views import generic
from core.models import Card
from django.contrib.auth.mixins import LoginRequiredMixin


class CardView(LoginRequiredMixin, generic.DetailView):
    """
    DetailView used for a Card.

    """

    model = Card
    template_name = "core/card.html"
    login_url = "users:login"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])
