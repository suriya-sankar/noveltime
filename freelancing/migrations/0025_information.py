# Generated by Django 3.0.8 on 2020-07-07 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancing', '0024_auto_20200708_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inform', models.TextField()),
            ],
        ),
    ]