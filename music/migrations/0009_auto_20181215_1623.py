# Generated by Django 2.1.2 on 2018-12-15 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_music_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_logo', models.CharField(max_length=240)),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('video_title', models.CharField(max_length=500)),
                ('video_genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Music',
        ),
        migrations.AddField(
            model_name='audio',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Video'),
        ),
    ]
