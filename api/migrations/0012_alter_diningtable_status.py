# Generated by Django 4.2.6 on 2024-04-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20240410_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diningtable',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied'), ('asking bill', 'Asking Bill')], default='available', max_length=11),
        ),
    ]
