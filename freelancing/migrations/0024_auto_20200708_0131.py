# Generated by Django 3.0.8 on 2020-07-07 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancing', '0023_auto_20200708_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_chappter',
            name='chapter_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='audio_story',
            name='story_title_pic',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='chappter',
            name='chapter_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='story',
            name='story_title_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
