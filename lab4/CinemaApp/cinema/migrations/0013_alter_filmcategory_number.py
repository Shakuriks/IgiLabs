# Generated by Django 4.2.1 on 2023-06-02 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0012_alter_filmcategory_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmcategory',
            name='number',
            field=models.IntegerField(),
        ),
    ]
