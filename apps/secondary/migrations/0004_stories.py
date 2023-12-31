# Generated by Django 4.2.7 on 2023-11-10 19:42

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0003_alter_history_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='stories_image/', verbose_name='Фотография')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Сторис',
                'verbose_name_plural': 'Сторисы',
            },
        ),
    ]
