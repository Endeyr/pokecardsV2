from users.views.register import RegisterView
from users.views.profile import ProfileView
from users.views.update_profile import UpdateProfileView
from users.views.update_user import UpdateUserView
from users.views.login import CustomLoginView
from users.views.password_change import CustomPasswordChangeView
from users.views.password_reset import CustomPasswordResetView

__all__ = [
    RegisterView,
    ProfileView,
    UpdateUserView,
    UpdateProfileView,
    CustomLoginView,
    CustomPasswordChangeView,
    CustomPasswordResetView,
]
