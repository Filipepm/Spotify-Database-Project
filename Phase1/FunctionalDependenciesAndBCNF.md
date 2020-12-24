**Functional Dependencies for CMSC 508 Team 12**

_Prior to BCNF_

* Username -> playlistName
 
* PlaylistName -> songTitle

* SongTitle -> artistName, albumTitle, playlistName

* AlbumTitle -> artistName

* ArtistName -> songTitle, albumTitle

_BCNF Breakdown:_ 

The superkeys for the functional dependencies are {(Username), (Username, PlaylistName), (Username, SongTitle), (Username, AlbumTitle), (Username, ArtistName), (Username, PlaylistName, SongTitle), (Username, PlaylistName, AlbumTitle), (Username, PlaylistName, ArtistName), and etc}

The candidate key is Username. 

The FD of Username -> PlaylistName is in BCNF making
R1(Username,PlaylistName) and R2(PlaylistName, SongTitle, AlbumTitle, ArtistName) 


The FD of PlaylistName-> songTitle which violates BCNF so we decompose it to 
R1(Username,PlaylistName) R2(PlaylistName, SongTitle), and R3(SongTitle,  AlbumTitle, ArtistName)

The FD of SongTitle -> artistName, albumTitle, playlistName which violates BCNF aswell so decomposes to R1(Username, PlaylistName) R2(PlaylistName, SongTitle) R3(SongTitle, ArtistName, AlbumTitle, PlaylistName)

The FD of AlbumTitle -> ArtistName violates the BCNF so we decompose it to R1(Username, PlaylistName) R2(PlaylistName, SongTitle) R3(SongTitle, ArtistName, AlbumTitle, PlaylistName) R4(AlbumTitle, ArtistName)

The FD of ArtistName -> songTitle, albumTitle violates the BCNF so we decompose it to R1(Username, PlaylistName) R2(PlaylistName, SongTitle) R3(SongTitle, ArtistName, AlbumTitle, PlaylistName) R4(AlbumTitle, ArtistName)
R5(ArtistName, SongTitle, AlbumTitle) 


**All relations are now in BCNF**


 