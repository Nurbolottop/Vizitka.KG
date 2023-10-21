# Generated by Django 4.2.6 on 2023-10-20 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_image_alter_stories_image'),
        ('category', '0008_thirdblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='FourBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('four', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='four_category', to='blog.category', verbose_name='Категория которую будете отображать')),
            ],
            options={
                'verbose_name': 'Четвертый блог',
                'verbose_name_plural': 'Четвертый блог',
            },
        ),
    ]
