# Generated by Django 4.2.6 on 2023-10-13 23:09

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='blog_images/', verbose_name='Основная фотография')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_images', to='blog.blog', verbose_name='Автомобиль')),
            ],
            options={
                'verbose_name': 'Картинка новстей',
                'verbose_name_plural': 'Картинки новстей',
            },
        ),
    ]
