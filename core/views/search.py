from django.views import generic


class SearchView(generic.TemplateView):
    """
    TemplateView used for our search page.

    """

    template_name = "core/search.html"
