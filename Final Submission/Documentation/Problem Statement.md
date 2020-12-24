Steven Hayes
Kevin Morales
Felipe Mourao
Database Theory
9/30/2020

# Problem Statement

Our project seeks to create a simple, no bloatware, easy to use music listening and discovery service. The end goal is a product that allows users to listen, rate and collaborate with other users on what music they like. The scope of this project is to create a database, as reflected in our ERD, consisting of five major entities, users, user created playlists, artists, albums and songs. One entity will consist of users, which are simply the people who use the database to find search for music and to add that music to playlists. Users will be related to other users via a friends list, and to playlists that they have created. Playlists are the lists of songs that users can create to revisit later. Playlists are be tied to songs that exist on the playlist and the user who created it. Another entity is the song entity, which is the smallest unit of music that our database allows a user to interact with.  Songs are connected to the artist that wrote the song and the album that the song released as a part of. An album is a set of songs that the artist who created the album released at the same time, each album is only linked to the artist who created it. The last entity is the artist, for the purposes of this database, the artist is just the name of the band who wrote a song or album. For our database, normal users will only have two options to make changes to the database itself, and that is to create new playlists from songs that already exist in the database or to add another currently existing user as a friend. All other database functions, such as maintenance, adding new music, or new functionality will fall to an admin user, who has access to the database itself via MySQLWorkbench. 

To facilitate creating this database, we created a list of queries to help ourselves determine what the database would look like and how it would operate. These queries became the basis for how we saw not only the relationships between elements of the database, but also how the user would interact with the database and with other users. The list of queries is as follows

1. What is the user's favorite song:
Select favoriteSong from User1 where userName = 'Kevin';

2. Who are the users friends: (Kevin)
Select friendName from Friends where userName = 'Kevin';

 3. Add a friend for a user
Insert into Friends values ('Kevin', 'Jenn');

4. Who is the artist for a song
Select artistName From Song where songTitle = 'Beat It';

5. Who is the artist for an album 
Select artistName from Album where albumTitle = 'Bad';

6. Update a user’s favorite song
Update User1 Set favoriteSong = 'God\'s Plan' Where userName = 'Kevin';

7. Which artists have recorded songs under 3 minutes, and how many songs was that?
Select x.artistName, count(*) as 'Number of Songs Under 3 Min'
from (select ar.artistName, s.duration 
from Song s inner join Artist ar on s.artistName = ar.artistName where duration < 3)as x group by x.artistName;

8. Create a new Playlist for the user 
Insert into UserPlaylists Values ('New Playlist', 'Kevin', NULL);

9. Add a song to the playlist: Have to alter Tables
Insert into Playlist values ('Kevins Playlist', 'God\'s Plan');

10. Which artist(s) have recorded the most songs
Select ar.artistName, count(*) as 'Number of Songs' 
From Song s inner join Artist ar on s.artistName = ar.artistName
Group By ar.artistName having count(*) = (
select max(songCount) from(select ar.artistName, count(*) as songCount 
from Song s inner join Artist ar on s.artistName = ar.artistName 
group by ar.artistName) as temp);

11. How long does a song last 
Select duration from Song where songTitle = 'Bad';

12. What genre is a song (using an artist's genre)
Select genreName as Genre from Artist a inner join Song s on a.artistName = s.artistName where songTitle = 'God\'s Plan';

13. How many albums has an artist released
Select Count(AlbumTitle) as NumberOfAlbums From Album as al inner join Artist as ar on al.artistName = ar.artistName where al.artistName = 'Drake';

14. How many songs are on an album 
Select Count(songTitle) as NumberOfSongs From Song where albumTitle = 'Views';

15. What is the playlist owner's username
Select userName from UserPlaylists where playListName = 'Kevins Playlist';

16 Which artist(s) have recorded the least songs
Select ar.artistName, count(*) as 'Number of Songs' 
From Song s inner join Artist ar on s.artistName = ar.artistName
Group By ar.artistName having count(*) = (
select min(songCount) from(select ar.artistName, count(*) as songCount 
from Song s inner join Artist ar on s.artistName = ar.artistName 
group by ar.artistName) as temp);


17. In which year or years were the most albums produced:
Select year , count(*) as 'Number of Albums' from Album 
group by year having count(*) = (select max(count) 
from (select year, count(*) as count from Album group by year)as x);

18. How would the use describe their playList:
Select description from UserPlaylists where userName = 'Kevin';

19. Upload a song/album the user wrote
Insert into Artist values('Kevin', 'R&B', NULL);
Insert into Album values ('SQL The Album', 'Kevin', 2020); -- Album
Insert into Song values ('SQLite', 2.5, 'Kevin', 'SQL The Album'); -- Song

20. What year did an album come out
Select year from Album where albumTitle = 'Views';

We are hoping to create a user experience that consists of the following basic interaction loop with the user. As a first step when the user starts to interact with the database, they will have two options of how to proceed. First, the user can simply start listening to a currently existing playlist that is already in the database. Secondly, users can start the process of creating a new playlist or modifying a previously made playlist. If the user elects to listen to a currently existing playlist, which could either be a playlist created by themselves or another user, then they will be taken to the playlist, where they can access the songs to listen and view information about them. After finishing listening the user is returned to the first step of the process. If the user opts to create a new playlist or modify a currently extant playlist, they will then be able to access other parts of the database, specifically songs, artists and albums. The user can search through these three major entities to find new music to listen to. As a user finds songs they like, they can add them to their playlist. Once the user has completed their search, they can name their playlist, share it with friends, or just simply listen. After finishing the playlist creation process, the user will again be redirected to step one of the interaction process. 



