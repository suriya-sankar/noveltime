# Generated by Django 3.0.3 on 2020-07-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancing', '0020_audio_chappter_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_story',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
