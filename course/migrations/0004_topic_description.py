# Generated by Django 4.1.1 on 2022-11-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_topic_chapter_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default='', max_length=300),
        ),
    ]
