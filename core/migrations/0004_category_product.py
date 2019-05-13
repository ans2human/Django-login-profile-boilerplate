# Generated by Django 2.1.7 on 2019-02-21 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190220_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=True)),
                ('subcategories', models.ManyToManyField(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
        ),
    ]
