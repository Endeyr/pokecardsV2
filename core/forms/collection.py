from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models.collection import Collection


class CollectionForm(LoginRequiredMixin, forms.ModelForm):
    """
    Create a collection for the user
    """

    INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = self.INPUT_CLASSES

    class Meta:
        model = Collection
        fields = (
            "title",
            "description",
        )
