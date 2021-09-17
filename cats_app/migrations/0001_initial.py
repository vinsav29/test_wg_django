# Generated by Django 3.2.7 on 2021-09-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('color', models.CharField(choices=[('black', 'B'), ('white', 'W'), ('black & white', 'Bw'), ('red', 'R'), ('red & white', 'Rw'), ('red & black & white', 'Rbw')], max_length=30)),
                ('tail_length', models.IntegerField()),
                ('whiskers_length', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CatsColorsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('black', 'B'), ('white', 'W'), ('black & white', 'Bw'), ('red', 'R'), ('red & white', 'Rw'), ('red & black & white', 'Rbw')], max_length=30)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CatsStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tail_length_mean', models.IntegerField()),
                ('tail_length_median', models.IntegerField()),
                ('tail_length_mode', models.IntegerField()),
                ('whiskers_length_mean', models.IntegerField()),
                ('whiskers_length_median', models.IntegerField()),
                ('whiskers_length_mode', models.IntegerField()),
            ],
        ),
    ]