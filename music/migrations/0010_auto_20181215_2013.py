# Generated by Django 2.1.2 on 2018-12-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20181215_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_logo',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]