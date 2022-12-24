# Generated by Django 4.1.3 on 2022-12-10 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('user_image', models.ImageField(blank=True, null=True, unique=True, upload_to='profile_pics/')),
                ('user_bio', models.TextField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=125, null=True)),
                ('last_name', models.CharField(blank=True, max_length=125, null=True)),
                ('first_name', models.CharField(blank=True, max_length=125, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
