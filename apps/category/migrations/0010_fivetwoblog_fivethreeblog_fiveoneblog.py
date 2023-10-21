# Generated by Django 4.2.6 on 2023-10-20 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_image_alter_stories_image'),
        ('category', '0009_fourblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiveTwoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='five_two_category', to='blog.category', verbose_name='Категория которую будете отображать')),
            ],
            options={
                'verbose_name': 'Пятый блог - Второй пункт',
                'verbose_name_plural': 'Пятый блог - Второй пункт',
            },
        ),
        migrations.CreateModel(
            name='FiveThreeBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='five_three_category', to='blog.category', verbose_name='Категория которую будете отображать')),
            ],
            options={
                'verbose_name': 'Пятый блог - Третий пункт',
                'verbose_name_plural': 'Пятый блог - Третий пункт',
            },
        ),
        migrations.CreateModel(
            name='FiveOneBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='five_one_category', to='blog.category', verbose_name='Категория которую будете отображать')),
            ],
            options={
                'verbose_name': 'Пятый блог - Первый пункт',
                'verbose_name_plural': 'Пятый блог - Первый пункт',
            },
        ),
    ]
