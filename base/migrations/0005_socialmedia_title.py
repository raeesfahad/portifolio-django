# Generated by Django 4.0.6 on 2022-07-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_about_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
