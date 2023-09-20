from django.views import generic
from core.models import Collection
from django.contrib.auth.mixins import LoginRequiredMixin


class CollectionView(LoginRequiredMixin, generic.DetailView):
    """
    DetailView used for a Collection.
    """

    model = Collection
    template_name = "core/collection.html"
    login_url = "users:login"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])
