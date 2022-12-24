# Generated by Django 4.1.4 on 2022-12-11 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Articles', '0006_rename_title_articlemodel_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='articlemodel',
            name='Rasm',
        ),
        migrations.RemoveField(
            model_name='articlemodel',
            name='Slug',
        ),
        migrations.RemoveField(
            model_name='articlemodel',
            name='Title',
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='Ega',
            field=models.ForeignKey(default=1, help_text='MAQOLA EGASI', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='RASIM_UZ',
            field=models.ImageField(blank=True, help_text='MAQOLA RASIM', null=True, unique=True, upload_to='images/articles/'),
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='SARLAVHA',
            field=models.CharField(default=1, help_text='MAQOLA SARLAVHA', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articlemodel',
            name='TAKRORLANMASI_NOM',
            field=models.SlugField(default=2, help_text='TAKRORLANMAS NOM', unique=True),
            preserve_default=False,
        ),
    ]
