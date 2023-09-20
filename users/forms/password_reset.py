from django.contrib.auth.forms import PasswordResetForm


class UpdatePasswordResetForm(PasswordResetForm):
    INPUT_CLASSES = "w-full text-black text-2xl sm:text-3xl p-3 rounded-xl border border-solid border-slate-900 border-none"

    def __init__(self, *args, **kwargs):
        super(UpdatePasswordResetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = self.INPUT_CLASSES
