# Generated by Django 2.1.2 on 2018-12-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20181215_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_logo',
            field=models.FileField(default=True, upload_to='images'),
            preserve_default=False,
        ),
    ]