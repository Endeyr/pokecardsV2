# Generated by Django 4.2.5 on 2023-10-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_card_artist_alter_card_name_alter_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='hp',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
