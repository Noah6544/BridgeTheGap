# Generated by Django 4.1.1 on 2022-11-10 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='user',
        ),
    ]
