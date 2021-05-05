# Generated by Django 3.2 on 2021-05-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='accomplishment',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='challenges',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='how_we_build',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='inspiration',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='we_learned',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='what_it_does',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='whats_next',
            field=models.TextField(max_length=1000),
        ),
    ]