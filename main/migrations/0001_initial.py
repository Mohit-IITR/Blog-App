# Generated by Django 4.0.3 on 2022-04-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('small_desc', models.CharField(max_length=1000)),
                ('full_content', models.CharField(max_length=1000)),
            ],
        ),
    ]
