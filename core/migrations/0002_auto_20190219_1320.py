# Generated by Django 2.1.7 on 2019-02-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.FileField(upload_to='profiles/'),
        ),
    ]
