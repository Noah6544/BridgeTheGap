# Generated by Django 4.1.1 on 2022-11-09 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=100)),
                ('content', models.TextField(default='Content', max_length=10000)),
                ('chapter_covers', models.CharField(default='Chapter covers:', max_length=50)),
                ('summary', models.CharField(default='Chapter Summary:', max_length=500)),
                ('completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default="Let's Write Your First Program!", max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('explanation', models.TextField(default='Explanation')),
                ('chapter', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='ImportantInstructionContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important_content', models.TextField(default='', max_length=100)),
                ('chapter', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('correct_choice', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.question')),
            ],
        ),
    ]
