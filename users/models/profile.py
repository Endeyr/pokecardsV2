from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Our UserProfile model extends the built-in Django User Model
    """

    class Meta:
        verbose_name_plural = "Users' profile"

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, null=True, blank=True, default="")
    avatar = models.ImageField(default="default.jpg", upload_to="profile_pictures")
