# Generated by Django 2.0.3 on 2018-11-10 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', markdownx.models.MarkdownxField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('diary_log', models.TextField(default='2018-11-10 18:42:02.849348  Create diary')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='example group', max_length=40)),
                ('intro', models.CharField(default='no introduce', max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('profile', imagekit.models.fields.ProcessedImageField(default='group/img/default.jpg', upload_to='group/img')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenotes.Group'),
        ),
    ]