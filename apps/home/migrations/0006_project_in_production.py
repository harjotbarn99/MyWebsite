# Generated by Django 3.0.8 on 2021-01-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_project_on_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='in_production',
            field=models.BooleanField(default=False),
        ),
    ]
