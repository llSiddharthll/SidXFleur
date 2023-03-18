# Generated by Django 4.1.7 on 2023-03-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_link', models.URLField(blank=True, unique=True)),
                ('mod_name', models.CharField(max_length=50)),
                ('mod_android', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rom_name', models.CharField(max_length=50)),
                ('rom_link', models.URLField(blank=True, null=True, unique=True)),
                ('android', models.FloatField()),
                ('version', models.DateField()),
                ('bugs', models.CharField(max_length=100, null=True)),
                ('credit', models.CharField(max_length=150, null=True)),
                ('fw', models.CharField(max_length=50)),
                ('boot', models.CharField(max_length=50)),
            ],
        ),
    ]
