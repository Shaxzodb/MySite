# Generated by Django 4.1.4 on 2022-12-13 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0017_alter_articlemodel_likes'),
        ('Comments', '0008_alter_commentarticle_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentarticle',
            name='article_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='Articles.articlemodel'),
        ),
    ]