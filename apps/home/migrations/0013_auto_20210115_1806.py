# Generated by Django 3.0.8 on 2021-01-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210114_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='development_message',
            field=models.TextField(blank=True, default='In development.'),
        ),
        migrations.AddField(
            model_name='work',
            name='in_development',
            field=models.BooleanField(default=True),
        ),
    ]
