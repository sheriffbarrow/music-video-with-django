# Generated by Django 2.1.2 on 2018-12-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20181215_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='name',
            field=models.CharField(default=True, max_length=240),
            preserve_default=False,
        ),
    ]