# Generated by Django 4.2.7 on 2024-01-31 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_lohi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lohi',
            name='post',
        ),
    ]
