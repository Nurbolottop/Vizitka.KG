# Generated by Django 4.2.7 on 2024-01-16 00:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_site_descriptions_alter_magazine_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='descriptions',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст'),
        ),
    ]
