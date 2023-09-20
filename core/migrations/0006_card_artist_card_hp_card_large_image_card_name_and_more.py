# Generated by Django 4.2.4 on 2023-09-01 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_collection_card_collection_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='artist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='hp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='large_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='rarity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='set',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='small_image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='subtypes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='supertype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='types',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
