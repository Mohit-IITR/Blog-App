# Generated by Django 4.0.3 on 2022-05-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogs_tags_user_delete_blogdata_blogs_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
