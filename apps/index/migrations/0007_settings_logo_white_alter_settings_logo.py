# Generated by Django 4.2.7 on 2023-11-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_delete_stories'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='logo_white',
            field=models.ImageField(default=1, upload_to='logo/', verbose_name='Логотип для темного фона'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(upload_to='logo/', verbose_name='Логотип для темного фона'),
        ),
    ]