# Generated by Django 4.2.7 on 2023-11-10 18:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_settings_descriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
            ],
            options={
                'verbose_name': 'Рекламодателям',
                'verbose_name_plural': 'Рекламодателям',
            },
        ),
    ]
