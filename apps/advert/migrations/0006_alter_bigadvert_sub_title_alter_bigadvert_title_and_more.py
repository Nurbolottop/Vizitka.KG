# Generated by Django 4.2.6 on 2023-10-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_alter_bigadvert_image_alter_normaladvert_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigadvert',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AlterField(
            model_name='bigadvert',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='bigadvert',
            name='url_booking',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='normaladvert',
            name='url_booking',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='smalladvert',
            name='url_booking',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
    ]
