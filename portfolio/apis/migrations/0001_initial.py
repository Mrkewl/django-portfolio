# Generated by Django 4.0.3 on 2022-04-08 14:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image_url', models.TextField()),
                ('description', models.TextField()),
                ('theme', models.CharField(max_length=30)),
                ('screens_urls', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('key_contribtion', models.TextField()),
                ('logo_url', models.TextField(default='https://media.gaigai.com/2020/09/71103625-gaigai_weblogo_500pxw.png')),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('google_app_link', models.TextField()),
                ('apple_app_link', models.TextField()),
                ('picture_url', models.TextField()),
                ('hello', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('stack', models.TextField()),
                ('about_me', models.TextField()),
                ('profile_picture_url', models.TextField()),
            ],
        ),
    ]
