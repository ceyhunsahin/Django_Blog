# Generated by Django 3.2.11 on 2022-01-07 08:21

import blog_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20220104_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='django_1.jpg', upload_to=blog_app.models.user_directory_path),
        ),
    ]