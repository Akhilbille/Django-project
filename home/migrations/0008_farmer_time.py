# Generated by Django 3.2.6 on 2021-09-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210914_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
