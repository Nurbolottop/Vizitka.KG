# Generated by Django 4.2.7 on 2023-11-08 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_categories', '0003_thirdblog_secondblog_fourblog_fivetwoblog_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firstblog',
            options={'verbose_name': 'Изменить категорию для B1', 'verbose_name_plural': 'Изменить категорию для B1'},
        ),
        migrations.AlterModelOptions(
            name='fiveoneblog',
            options={'verbose_name': 'Изменить категорию для B5', 'verbose_name_plural': 'Изменить категорию для B5'},
        ),
        migrations.AlterModelOptions(
            name='fivethreeblog',
            options={'verbose_name': 'Изменить категорию для B7', 'verbose_name_plural': 'Изменить категорию для B7'},
        ),
        migrations.AlterModelOptions(
            name='fivetwoblog',
            options={'verbose_name': 'Изменить категорию для B6', 'verbose_name_plural': 'Изменить категорию для B6'},
        ),
        migrations.AlterModelOptions(
            name='fourblog',
            options={'verbose_name': 'Изменить категорию для B4', 'verbose_name_plural': 'Изменить категорию для B4'},
        ),
        migrations.AlterModelOptions(
            name='secondblog',
            options={'verbose_name': 'Изменить категорию для B2', 'verbose_name_plural': 'Изменить категорию для B2'},
        ),
        migrations.AlterModelOptions(
            name='thirdblog',
            options={'verbose_name': 'Изменить категорию для B3', 'verbose_name_plural': 'Изменить категорию для B3'},
        ),
    ]