# Generated by Django 2.1 on 2019-02-25 08:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190225_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 8, 48, 3, 940722)),
        ),
    ]