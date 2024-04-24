# Generated by Django 5.0.4 on 2024-04-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=155, unique=True, verbose_name='Assignment Code')),
                ('name', models.CharField(max_length=155, verbose_name='Assignment Name')),
                ('description', models.TextField(verbose_name='Assignment Description')),
                ('marks', models.PositiveIntegerField(verbose_name='Maximum Score')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('code', models.CharField(max_length=155, primary_key=True, serialize=False, verbose_name='Assignment Code')),
                ('name', models.CharField(max_length=155, verbose_name='Assignment Name')),
                ('description', models.TextField(verbose_name='Assignment Description')),
                ('score', models.PositiveIntegerField(default=0, verbose_name='Student Score')),
            ],
        ),
    ]
