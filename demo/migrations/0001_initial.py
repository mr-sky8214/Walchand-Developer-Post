# Generated by Django 3.2 on 2021-04-18 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=16)),
                ('verified', models.BooleanField(default=False)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='project/images/')),
                ('year', models.IntegerField()),
                ('domain', models.CharField(max_length=100)),
                ('guide', models.CharField(max_length=100)),
                ('inspiration', models.TextField(max_length=100)),
                ('what_it_does', models.TextField(max_length=500)),
                ('how_we_build', models.TextField(max_length=500)),
                ('challenges', models.TextField(max_length=500)),
                ('accomplishment', models.TextField(max_length=500)),
                ('we_learned', models.TextField(max_length=500)),
                ('whats_next', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=16)),
                ('photo', models.ImageField(upload_to='student/images')),
                ('github', models.URLField(blank=True)),
                ('linked_in', models.URLField(blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.project')),
                ('tech_label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.technology')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Student_notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.BooleanField(default=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.student')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.project')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.student')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Guide_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.BooleanField(default=False)),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.guide')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.guide')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.project')),
            ],
        ),
    ]
