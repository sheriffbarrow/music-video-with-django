# Generated by Django 2.1.2 on 2018-12-15 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_auto_20181215_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='videofile',
        ),
    ]
