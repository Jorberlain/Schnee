# Generated by Django 2.0.3 on 2018-11-20 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20181110_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='id_content',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='is_deal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_type',
            field=models.CharField(choices=[('M', 'Message'), ('F', 'Friend_Invitation'), ('G', 'Group_Invitation')], default='Message', max_length=12),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_msg', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_msg', to=settings.AUTH_USER_MODEL),
        ),
    ]
