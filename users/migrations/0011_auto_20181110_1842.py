# Generated by Django 2.0.3 on 2018-11-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_userinfo_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(blank=True, default='Undefined@example.com', max_length=70),
        ),
    ]
