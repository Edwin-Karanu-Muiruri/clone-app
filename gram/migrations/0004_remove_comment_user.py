# Generated by Django 3.0 on 2020-06-02 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
