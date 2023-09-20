from django.views import generic
from core.models import Card


class CardsView(generic.ListView):
    """
    ListView used for our cards.
    """

    model = Card
    template_name = "core/cards.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
