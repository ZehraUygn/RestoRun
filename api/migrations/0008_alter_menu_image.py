# Generated by Django 4.2.6 on 2024-03-30 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_category_menu_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, default='static/menu_images/brik.png', upload_to='static/menu_images/'),
        ),
    ]
