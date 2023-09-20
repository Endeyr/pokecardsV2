from django.views import generic


class AdvSearchView(generic.TemplateView):
    """
    TemplateView used for our advanced serach page

    **Template:**

    :template:'core/adv-search.html'
    """

    template_name = "core/adv-search.html"
