# Generated by Django 4.2.1 on 2023-06-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
