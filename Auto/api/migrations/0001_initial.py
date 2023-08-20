# Generated by Django 4.2.4 on 2023-08-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AutosPassport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.TextField(max_length=2)),
                ('number', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=23)),
                ('last_name', models.CharField(max_length=23)),
            ],
        ),
    ]