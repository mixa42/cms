# Generated by Django 4.1.7 on 2023-02-28 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_menu_timestamp_alter_menu_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 21, 42, 20, 164123)),
        ),
    ]
