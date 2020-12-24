-- 1. What is the user's favorite song:
Select favoriteSong from User1 where userName = 'Kevin';

-- 2. Who are the users friends: (Kevin)
Select friendName from Friends where userName = 'Kevin';

-- 3. Add a friend for a user
Insert into Friends values ('Kevin', 'Jenn');

-- 4. Who is the artist for a song
Select artistName From Song where songTitle = 'Beat It';

-- 5. Who is the artist for an album 
Select artistName from Album where albumTitle = 'Bad';

-- 6. Update a user’s favorite song
Update User1 Set favoriteSong = 'God\'s Plan' Where userName = 'Kevin';

-- 7. Which artists have recorded songs under 3 minutes, and how many songs was that?
Select x.artistName, count(*) as 'Number of Songs Under 3 Min'
from (select ar.artistName, s.duration 
from Song s inner join Artist ar on s.artistName = ar.artistName where duration < 3)as x group by x.artistName;

-- 8. Create a new Playlist for the user 
Insert into UserPlaylists Values ('New Playlist', 'Kevin', NULL);

-- 9. Add a song to the playlist: Have to alter Tables
Insert into Playlist values ('Kevins Playlist', 'God\'s Plan');

-- 10. Which artist(s) have recorded the most songs
Select ar.artistName, count(*) as 'Number of Songs' 
From Song s inner join Artist ar on s.artistName = ar.artistName
Group By ar.artistName having count(*) = (
select max(songCount) from(select ar.artistName, count(*) as songCount 
from Song s inner join Artist ar on s.artistName = ar.artistName 
group by ar.artistName) as temp);

-- 11. How long does a song last 
Select duration from Song where songTitle = 'Bad';

-- 12. What genre is a song (using an artist's genre)
Select genreName as Genre from Artist a inner join Song s on a.artistName = s.artistName where songTitle = 'God\'s Plan';

-- 13. How many albums has an artist released
Select Count(AlbumTitle) as NumberOfAlbums From Album as al inner join Artist as ar on al.artistName = ar.artistName where al.artistName = 'Drake';

-- 14 How many songs are on an album 
Select Count(songTitle) as NumberOfSongs From Song where albumTitle = 'Views';

-- 15. What is the playlist owner's username
Select userName from UserPlaylists where playListName = 'Kevins Playlist';

-- 16 Which artist(s) have recorded the least songs
Select ar.artistName, count(*) as 'Number of Songs' 
From Song s inner join Artist ar on s.artistName = ar.artistName
Group By ar.artistName having count(*) = (
select min(songCount) from(select ar.artistName, count(*) as songCount 
from Song s inner join Artist ar on s.artistName = ar.artistName 
group by ar.artistName) as temp);


-- 17. In which year or years were the most albums produced:
Select year , count(*) as 'Number of Albums' from Album 
group by year having count(*) = (select max(count) 
from (select year, count(*) as count from Album group by year)as x);

-- 18. How would the use describe their playList:
Select description from UserPlaylists where userName = 'Kevin';

-- 19. Upload a song/album the user wrote
Insert into Artist values('Kevin', 'R&B', NULL);
Insert into Album values ('SQL The Album', 'Kevin', 2020); -- Album
Insert into Song values ('SQLite', 2.5, 'Kevin', 'SQL The Album'); -- Song

-- 20. What year did an album come out
Select year from Album where albumTitle = 'Views';

