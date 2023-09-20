from django.views import generic
from core.forms import CollectionForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateCollectionView(LoginRequiredMixin, generic.FormView):
    """
    FormView used for our create collection page

    """

    template_name = "core/create-collection.html"
    form_class = CollectionForm
    success_url = reverse_lazy("core:collections")
    login_url = "users:login"

    def form_valid(self, form):
        form.save()
        return super(CreateCollectionView, self).form_valid(form)
