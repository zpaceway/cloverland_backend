# Generated by Django 4.2 on 2023-04-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('phone', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=128)),
                ('secret', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
