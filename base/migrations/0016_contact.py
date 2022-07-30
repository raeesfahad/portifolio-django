# Generated by Django 4.0.6 on 2022-07-29 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_services_icon_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('subject', models.CharField(max_length=90)),
                ('message', models.TextField()),
            ],
        ),
    ]