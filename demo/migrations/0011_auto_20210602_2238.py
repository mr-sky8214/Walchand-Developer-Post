# Generated by Django 3.2 on 2021-06-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_auto_20210601_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='linked_in',
            field=models.URLField(blank=True, null=True),
        ),
    ]
