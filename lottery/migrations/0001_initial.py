# Generated by Django 4.0.2 on 2023-04-23 18:08

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', tinymce.models.HTMLField()),
                ('address', models.CharField(max_length=128)),
                ('private_key', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('ends_at', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'lotteries',
            },
        ),
    ]
