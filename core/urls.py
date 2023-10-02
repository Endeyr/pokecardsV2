from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("search/", views.SearchView.as_view(), name="search"),
    path(
        "collection/create/",
        views.CreateCollectionView.as_view(),
        name="create_collection",
    ),
    path("collection/<str:slug>/", views.CollectionView.as_view(), name="collection"),
    path("collections/", views.CollectionsView.as_view(), name="collections"),
    path("card/<str:id>/", views.CardView.as_view(), name="card"),
    path("cards/", views.CardsView.as_view(), name="cards"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("add_card/", views.add_card, name="add_card"),
    path("remove_card/<str:id>", views.remove_card, name="remove_card"),
    path("send_mail/", views.send_mail, name="send_mail"),
]
