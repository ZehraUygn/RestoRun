# Generated by Django 4.2.6 on 2024-04-28 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_order_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_acc',
        ),
        migrations.DeleteModel(
            name='RestaurantSettings',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
