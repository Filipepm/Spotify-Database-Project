from django.db import models

class User(models.Model):
	userName = models.CharField(max_length=25)
	password = models.CharField(max_length=25)
	userAge = models.CharField(max_length=2)
	recentlyListened = models.CharField(max_length=25)
	class Meta:
		db_table = "user"

class Playlist(models.Model):
	playlistName = models.CharField(max_length=25)
	userName = models.CharField(max_length=25)
	class Meta:
		db_table = "playlist"

class Friends(models.Model):
	userName = models.CharField(max_length=25)
	friendName = models.CharField(max_length=25)
	class Meta:
		db_table = "friend"

class Song(models.Model):
	songTitle = models.CharField(max_length=25)
	duration = models.CharField(max_length=5)
	artistName = models.CharField(max_length=25)
	albumTitle = models.CharField(max_length=25)
	class Meta:
		db_table = "song"

class Album(models.Model):
	artistName = models.CharField(max_length=25)
	albumTitle = models.CharField(max_length=25)
	year = models.CharField(max_length=25)
	class Meta:
		db_table = "album"

class Artist(models.Model):
	artistName = models.CharField(max_length=25)
	genreName = models.CharField(max_length=25)
	description = models.CharField(max_length=100)
	class Meta:
		db_table = "artist"
