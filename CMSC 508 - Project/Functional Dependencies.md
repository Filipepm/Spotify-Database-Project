
**Functional Dependencies for CMSC 508 Team 12**

-   User -> userName, playlistName
	--Primary key - userName
    
-  Friends -> userName, friendName,
	--Primary key - userName, friendName   
    
-   UserPlaylist -> playlistName, userName, playlistSize
--Primary key - playlistName

- Playlist -> playlistName, songName
--	Primary key - playlistName, songName
    
-   Song -> songTitle, artistName, albumTitle, duration
--	Primary key - songTitle
    
-   Album -> albumTitle, artistname, year
--Primary key - albumTitle
    
-   Artist -> artistName, genre, description
--Primary key - artistName
    
