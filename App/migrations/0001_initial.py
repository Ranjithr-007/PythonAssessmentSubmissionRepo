# Generated by Django 4.2.7 on 2024-05-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('stars', models.IntegerField()),
                ('forks', models.IntegerField()),
            ],
        ),
    ]
