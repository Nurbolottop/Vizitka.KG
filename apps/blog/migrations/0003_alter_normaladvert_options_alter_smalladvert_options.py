# Generated by Django 4.2.7 on 2023-11-08 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bigadvert_normaladvert_smalladvert'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normaladvert',
            options={'verbose_name': 'Добавить рекламу среднего масштаба ', 'verbose_name_plural': 'Добавить рекламу среднего масштаба'},
        ),
        migrations.AlterModelOptions(
            name='smalladvert',
            options={'verbose_name': 'Добавить рекламу среднего масштаба', 'verbose_name_plural': 'Добавить рекламу среднего масштаба'},
        ),
    ]
