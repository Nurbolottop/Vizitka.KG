# Generated by Django 4.2.6 on 2023-10-19 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_image_alter_stories_image'),
        ('category', '0006_rename_first_firstblog_category_titlee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstblog',
            name='category_titlee',
        ),
        migrations.AddField(
            model_name='firstblog',
            name='first',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_title', to='blog.category', verbose_name='Категория которую будете отображать'),
        ),
    ]
