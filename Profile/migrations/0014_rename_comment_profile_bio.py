# Generated by Django 4.1.4 on 2022-12-12 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0013_remove_profile_user_bio_profile_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='comment',
            new_name='bio',
        ),
    ]
