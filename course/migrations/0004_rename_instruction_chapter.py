# Generated by Django 4.1.1 on 2022-11-07 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_question_explanation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instruction',
            new_name='Chapter',
        ),
    ]