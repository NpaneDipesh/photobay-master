# Generated by Django 3.1.1 on 2020-09-12 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='save_count',
        ),
    ]