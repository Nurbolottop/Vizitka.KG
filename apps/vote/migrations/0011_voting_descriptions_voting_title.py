# Generated by Django 4.2.7 on 2023-12-18 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0010_voting'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='descriptions',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voting',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
