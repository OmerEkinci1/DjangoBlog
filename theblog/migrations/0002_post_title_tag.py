# Generated by Django 3.0.6 on 2020-06-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blogum.net', max_length=255),
        ),
    ]
