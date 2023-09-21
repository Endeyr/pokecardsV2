from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):
    """
    Need a field for each model field
    """

    INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"

    name = forms.CharField(
        label="Name",
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Full Name", "class": INPUT_CLASSES}
        ),
    )

    email = forms.EmailField(
        label="Email",
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": INPUT_CLASSES,
            }
        ),
    )

    telephone = forms.CharField(
        label="Telephone",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Phone Number",
                "autocomplete": "off",
                "class": INPUT_CLASSES,
            }
        ),
    )

    message = forms.CharField(
        label="Message",
        max_length=1000,
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Message",
                "class": INPUT_CLASSES,
            }
        ),
    )

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "telephone",
            "message",
        )
