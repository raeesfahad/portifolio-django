# Generated by Django 4.0.6 on 2022-07-29 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_skills_prcentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resp', models.CharField(max_length=900)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('to', models.DateField(verbose_name='from')),
                ('date_from', models.DateField(verbose_name='to')),
                ('employer', models.CharField(max_length=200, null=True)),
                ('responsibility', models.ManyToManyField(to='base.responsibility')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='achivements',
            field=models.ManyToManyField(to='base.responsibility'),
        ),
        migrations.AddField(
            model_name='me',
            name='experience',
            field=models.ManyToManyField(to='base.experience'),
        ),
    ]