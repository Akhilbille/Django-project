# Generated by Django 3.2.6 on 2021-09-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_farmer_supporting_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='supporting_images',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
