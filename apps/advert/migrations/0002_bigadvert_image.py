# Generated by Django 4.2.6 on 2023-10-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigadvert',
            name='image',
            field=models.ImageField(default=1, upload_to='images_advert', verbose_name='Фотографии'),
            preserve_default=False,
        ),
    ]
