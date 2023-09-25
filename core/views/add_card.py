from core.models import Card, Collection
from django.http import HttpResponse


def add_card(request):
    if request.method == "POST":
        collection = Collection.objects.get(user=request.user)
        cards = request.POST.getlist("card_id")
        for card in cards:
            try:
                card_obj = Card.objects.get(id=card)
                collection.cards.add(card_obj)
            except Card.DoesNotExist:
                card_obj = Card(id=card)
                card_obj.save()
                collection.cards.add(card_obj)
        return HttpResponse(f"Are these your card? - {cards}")
