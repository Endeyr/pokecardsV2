from django.views import generic
from core.models import Card
from django.contrib.auth.mixins import LoginRequiredMixin


class CardsView(LoginRequiredMixin, generic.ListView):
    """
    ListView used for our cards.
    """

    model = Card
    template_name = "core/cards.html"
    paginate_by = 10
    login_url = "users:login"

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
