from django.views import generic
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class ContactView(SuccessMessageMixin, generic.FormView):
    """
    TemplateView used for our contact page.

    """

    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("core:contact")
    success_message = "Message Sent!"
