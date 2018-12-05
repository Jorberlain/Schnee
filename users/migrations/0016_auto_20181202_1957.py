# Generated by Django 2.0.3 on 2018-12-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20181120_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_type',
            field=models.CharField(choices=[('M', 'Message'), ('F', 'Friend_Invitation'), ('G', 'Group_Invitation')], default='Message', max_length=20),
        ),
    ]
