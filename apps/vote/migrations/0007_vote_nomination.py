# Generated by Django 4.2.7 on 2023-12-17 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_alter_vote_unique_together_vote_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='nomination',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='vote.nomination', verbose_name='Номинация'),
            preserve_default=False,
        ),
    ]
