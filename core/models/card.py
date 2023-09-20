from django.db import models


class Card(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=10,
    )

    name = models.CharField(max_length=100, blank=True, null=True)

    supertype = models.CharField(max_length=100, blank=True, null=True)

    subtypes = models.CharField(max_length=100, blank=True, null=True)

    set = models.CharField(max_length=100, blank=True, null=True)

    hp = models.IntegerField(null=True, blank=True)

    rarity = models.CharField(max_length=100, blank=True, null=True)

    artist = models.CharField(max_length=100, blank=True, null=True)

    number = models.CharField(max_length=100, blank=True, null=True)

    types = models.CharField(max_length=100, blank=True, null=True)

    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=8)

    small_image = models.URLField(blank=True, null=True)

    large_image = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cards"

    def __str__(self):
        return f"{self.id}"
