# Generated by Django 4.2.7 on 2023-11-14 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_delete_magazineimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='magazine',
            old_name='document',
            new_name='pdf',
        ),
    ]
