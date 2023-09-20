from django import forms
from users.models.profile import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"


class UpdateProfileForm(forms.ModelForm):
    """
    Update the Profile attached to each user
    """

    bio = forms.CharField(
        label="Bio",
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "*Write a bio...",
                "class": INPUT_CLASSES,
                "cols": "18",
                "rows": "5",
            }
        ),
    )

    avatar = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.FileInput(attrs={"class": INPUT_CLASSES}),
    )

    class Meta:
        model = Profile
        fields = (
            "bio",
            "avatar",
        )
