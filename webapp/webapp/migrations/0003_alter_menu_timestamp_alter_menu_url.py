# Generated by Django 4.1.7 on 2023-02-28 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_menu_timestamp_alter_menu_parent_alter_menu_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 19, 43, 12, 568865)),
        ),
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка'),
        ),
    ]
