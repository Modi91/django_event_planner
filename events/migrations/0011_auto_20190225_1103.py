# Generated by Django 2.1 on 2019-02-25 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20190225_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='posture',
            new_name='poster',
        ),
    ]
