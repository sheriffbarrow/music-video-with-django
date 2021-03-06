# Generated by Django 2.1.2 on 2018-12-11 19:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20181209_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='album_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.CharField(default='No artist name', max_length=250),
        ),
        migrations.AddField(
            model_name='song',
            name='date_uploaded',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='No genre', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='song',
            field=models.FileField(default=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='file_type',
            field=models.CharField(default='No file type', max_length=10),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(default='No song title', max_length=250),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
