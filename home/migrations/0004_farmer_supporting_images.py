# Generated by Django 3.2.6 on 2021-09-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_side_bar_icon_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='supporting_images',
            field=models.ImageField(default='no image', upload_to='pics'),
        ),
    ]