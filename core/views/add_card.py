from core.models import Card, Collection
from django.shortcuts import redirect
from pokemontcgsdk import Card as PokemonCard


def add_card(request):
    if request.method == "POST":
        collection = Collection.objects.get(id=request.POST.get("collection_id"))
        cards = request.POST.getlist("card_id")
        for card in cards:
            try:
                card_obj = Card.objects.get(id=card)
                collection.cards.add(card_obj)
            except Card.DoesNotExist:
                card_api = PokemonCard.find(card)
                card_obj = Card(id=card)
                card_obj.artist = card_api.artist
                card_obj.hp = card_api.hp
                card_obj.large_image = card_api.images.large
                card_obj.name = card_api.name
                card_obj.number = card_api.number

                if card_api.tcgplayer.prices is None:
                    card_obj.price = "NA"
                elif card_api.tcgplayer.prices.normal:
                    card_obj.price = card_api.tcgplayer.prices.normal.market
                elif card_api.tcgplayer.prices.holofoil:
                    card_obj.price = card_api.tcgplayer.prices.holofoil.market
                elif card_api.tcgplayer.prices.reverseHolofoil:
                    card_obj.price = card_api.tcgplayer.prices.reverseHolofoil.market
                elif card_api.tcgplayer.prices.unlimited:
                    card_obj.price = card_api.tcgplayer.prices.unlimited.market
                elif card_api.tcgplayer.prices.unlimitedHolofoil:
                    card_obj.price = card_api.tcgplayer.prices.unlimitedHolofoil.market
                else:
                    card_obj.price = 0.00

                card_obj.rarity = card_api.rarity
                card_obj.set = card_api.set.name
                card_obj.small_image = card_api.images.small
                card_obj.subtypes = ", ".join(card_api.subtypes)
                card_obj.supertype = card_api.supertype
                card_obj.types = ", ".join(card_api.types)
                card_obj.save()
                collection.cards.add(card_obj)
        return redirect("core:collection", slug=collection.slug)
