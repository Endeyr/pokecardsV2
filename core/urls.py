from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("adv_search/", views.AdvSearchView.as_view(), name="adv_search"),
    path(
        "collection/create/",
        views.CreateCollectionView.as_view(),
        name="create_collection",
    ),
    path("collection/<str:slug>/", views.CollectionView.as_view(), name="collection"),
    path("collections/", views.CollectionsView.as_view(), name="collections"),
    path("card/<str:slug>/", views.CardView.as_view(), name="card"),
    path("cards/", views.CardsView.as_view(), name="cards"),
]
