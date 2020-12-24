# Generated by Django 2.0.7 on 2020-11-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=25)),
                ('albumTitle', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=25)),
                ('genreName', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'artist',
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=25)),
                ('friendName', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'friend',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistName', models.CharField(max_length=25)),
                ('userName', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'playlist',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songTitle', models.CharField(max_length=25)),
                ('duration', models.CharField(max_length=5)),
                ('artistName', models.CharField(max_length=25)),
                ('albumTitle', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'song',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('userAge', models.CharField(max_length=2)),
                ('recentlyListened', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]