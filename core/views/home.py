from django.views import generic


class HomeView(generic.TemplateView):
    """
    TemplateView used for our home page

    **Template:**

    :template:'core/index.html'
    """

    template_name = "core/index.html"