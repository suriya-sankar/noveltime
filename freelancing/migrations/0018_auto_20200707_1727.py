# Generated by Django 3.0.3 on 2020-07-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancing', '0017_auto_20200707_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='chappter',
            name='total_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chappter',
            name='user_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chappter',
            name='user_rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
