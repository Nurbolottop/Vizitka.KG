# Generated by Django 4.2.7 on 2023-12-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0008_advert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
