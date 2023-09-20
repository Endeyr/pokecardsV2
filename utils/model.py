import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models


class Model(models.Model):
    """
    Used in every db entry
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4)

    """
    abstract = True means we can inherit from this model
    """

    class Meta:
        abstract = True