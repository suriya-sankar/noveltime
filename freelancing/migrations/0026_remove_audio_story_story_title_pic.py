# Generated by Django 3.0.8 on 2020-07-07 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancing', '0025_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_story',
            name='story_title_pic',
        ),
    ]
