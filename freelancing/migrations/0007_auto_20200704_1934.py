# Generated by Django 3.0.3 on 2020-07-04 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancing', '0006_auto_20200704_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chappter',
            name='chapter_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
