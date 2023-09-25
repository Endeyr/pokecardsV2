from django.views import generic


class HomeView(generic.TemplateView):
    """
    View used for our home page
    """

    template_name = "core/index.html"
