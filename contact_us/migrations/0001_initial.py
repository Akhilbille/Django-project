# Generated by Django 3.2.6 on 2021-09-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_US',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('Subject', models.CharField(max_length=250)),
                ('Message', models.CharField(max_length=250)),
            ],
        ),
    ]