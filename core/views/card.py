from django.views import generic
from core.models import Card


class CardView(generic.DetailView):
    """
    DetailView used for a Card.

    """

    model = Card
    template_name = "core/card.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])
