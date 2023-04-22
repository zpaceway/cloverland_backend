# Generated by Django 4.2 on 2023-04-22 19:39

from django.db import migrations, models
import utils.common


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_alter_lottery_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='id',
            field=models.CharField(default=utils.common.PrefixedShortUuidGenerator.generate, max_length=36, primary_key=True, serialize=False),
        ),
    ]
