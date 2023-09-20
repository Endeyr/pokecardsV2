from django.db import models
from utils.model import Model
from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
)
from django.contrib.auth.models import User
from core.models.card import Card


class Collection(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cards = models.ManyToManyField(Card, blank=True)

    class Meta:
        verbose_name_plural = "Collections"
