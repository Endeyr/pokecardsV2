from core.models import Card, Collection
from django.shortcuts import redirect, get_object_or_404


def remove_card(request, id):
    if request.method == "POST":
        print(request.POST)
        collection = Collection.objects.get(id=request.POST.get("collection_id"))
        card = get_object_or_404(Card, id=id)
        collection.cards.remove(card)
        return redirect("core:collection", slug=collection.slug)
