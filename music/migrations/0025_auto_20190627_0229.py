# Generated by Django 2.1.2 on 2019-06-27 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0024_auto_20190625_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_logo',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]