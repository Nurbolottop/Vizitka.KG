# Generated by Django 4.2.6 on 2023-10-19 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firstblog',
            old_name='category_title',
            new_name='category_titlee',
        ),
    ]
