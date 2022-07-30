# Generated by Django 4.0.6 on 2022-07-18 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField(max_length=500)),
                ('title', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=20)),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('enrolled_date', models.DateField(verbose_name='from')),
                ('graduation_date', models.DateField(verbose_name='to')),
                ('currently_enrolled', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level_prcentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=200, null=True)),
                ('twitter', models.CharField(max_length=200, null=True)),
                ('instagram', models.CharField(max_length=200, null=True)),
                ('linkedin', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taglines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.about')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.education')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.skills')),
                ('social_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.socialmedia')),
                ('tagline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.taglines')),
            ],
        ),
    ]