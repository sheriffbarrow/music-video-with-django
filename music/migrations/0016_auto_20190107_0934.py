# Generated by Django 2.1.2 on 2019-01-07 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0015_video_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='audio',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]