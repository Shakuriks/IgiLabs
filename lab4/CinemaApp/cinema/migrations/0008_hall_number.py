# Generated by Django 4.2.1 on 2023-06-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_hall_session_alter_film_poster_alter_film_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
