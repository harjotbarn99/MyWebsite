# Generated by Django 4.1.5 on 2023-01-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='experience',
            name='place',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='experience',
            name='position',
            field=models.CharField(max_length=250),
        ),
    ]
