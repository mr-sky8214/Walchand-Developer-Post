# Generated by Django 2.2 on 2021-06-16 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0013_auto_20210607_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='batch',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='sem',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_guide',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_guide_notification',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_student_notifications',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_technology',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
