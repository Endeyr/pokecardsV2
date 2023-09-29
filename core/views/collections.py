from django.views import generic
from core.models import Collection
from django.contrib.auth.mixins import LoginRequiredMixin


class CollectionsView(LoginRequiredMixin, generic.ListView):
    """
    ListView used for our collections.
    """

    model = Collection
    template_name = "core/collections.html"
    paginate_by = 10
    login_url = "users:login"

    def get_queryset(self):
        user = self.request.user
        collection = Collection.objects.filter(user=user)
        return collection.active().order_by("-created")
