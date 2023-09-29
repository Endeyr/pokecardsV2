from core.views.home import HomeView
from core.views.search import SearchView
from core.views.create_collection import CreateCollectionView
from core.views.collection import CollectionView
from core.views.collections import CollectionsView
from core.views.card import CardView
from core.views.cards import CardsView
from core.views.contact import ContactView
from core.views.add_card import add_card
from core.views.remove_card import remove_card

__all__ = [
    HomeView,
    CreateCollectionView,
    CollectionView,
    CollectionsView,
    CardView,
    CardsView,
    SearchView,
    ContactView,
    remove_card,
    add_card,
]
