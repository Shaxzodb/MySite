# Generated by Django 4.1.4 on 2022-12-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_alter_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(default=1, upload_to='profile_pics/'),
            preserve_default=False,
        ),
    ]