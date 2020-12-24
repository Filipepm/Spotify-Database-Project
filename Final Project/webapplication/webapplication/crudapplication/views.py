from django.shortcuts import render, redirect
from crudapplication.forms import UserForm , PlaylistForm , FriendsForm , SongForm
from crudapplication.models import User , Playlist , Friends , Song

# ------------------ User -----------------------#
def userr(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = UserForm()
    return render(request, "index.html", {'form':form})

def show(request):
    users = User.objects.all()
    return  render(request,"show.html",{'users': users})

def edit(request, id):
    user = User.objects.get(id=id)
    return  render(request,"edit.html",{'user' : user})

def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance= user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return  render(request,"edit.html",{'user': user})

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/show")
# ---------------------------------------------------#

# ------------------ Playlist -----------------------#
def playlistt(request):
    if request.method == "POST":
        formplaylist = PlaylistForm(request.POST)
        if formplaylist.is_valid():
            try:
                formplaylist.save()
                return redirect("/show_playlist")
            except:
                pass
    else:
        formplaylist = PlaylistForm()
    return render(request, "index_playlist.html", {'formplaylist':formplaylist})

def showPlaylist(request):
    playlists = Playlist.objects.all()
    return  render(request,"show_playlist.html",{'playlists': playlists})

def editPlaylist(request, id):
    playlist = Playlist.objects.get(id=id)
    return  render(request,"edit_playlist.html",{'playlist' : playlist})

def updatePlaylist(request, id):
    playlist = Playlist.objects.get(id=id)
    formplaylist = PlaylistForm(request.POST, instance= playlist)
    if formplaylist.is_valid():
        formplaylist.save()
        return redirect('/show_playlist')
    return  render(request,"edit_playlist.html",{'playlist': playlist})

def deletePlaylist(request, id):
    playlist = Playlist.objects.get(id=id)
    playlist.delete()
    return redirect("/show_playlist")
# ---------------------------------------------------#

# ------------------ Friend -----------------------#
def friendd(request):
    if request.method == "POST":
        formfriend = FriendsForm(request.POST)
        if formfriend.is_valid():
            try:
                formfriend.save()
                return redirect("/show_friend")
            except:
                pass
    else:
        formfriend = FriendsForm()
    return render(request, "index_friend.html", {'formfriend':formfriend})

def showFriend(request):
    friends = Friends.objects.all()
    return  render(request,"show_friend.html",{'friends': friends})

def editFriend(request, id):
    friend = Friends.objects.get(id=id)
    return  render(request,"edit_friend.html",{'friend' : friend})

def updateFriend(request, id):
    friend = Friends.objects.get(id=id)
    formfriend = FriendsForm(request.POST, instance= friend)
    if formfriend.is_valid():
        formfriend.save()
        return redirect('/show_friend')
    return  render(request,"edit_friend.html",{'friend': friend})

def deleteFriend(request, id):
    friend = Friends.objects.get(id=id)
    friend.delete()
    return redirect("/show_friend")
# ---------------------------------------------------#

# ------------------ Song -----------------------#
def songg(request):
    if request.method == "POST":
        formsong = SongForm(request.POST)
        if formsong.is_valid():
            try:
                formsong.save()
                return redirect("/show_song")
            except:
                pass
    else:
        formsong = SongForm()
    return render(request, "index_song.html", {'formsong':formsong})

def showSong(request):
    songs = Song.objects.all()
    return  render(request,"show_song.html",{'songs': songs})

def editSong(request, id):
    song = Song.objects.get(id=id)
    return  render(request,"edit_song.html",{'song' : song})

def updateSong(request, id):
    song = Song.objects.get(id=id)
    formsong = SongForm(request.POST, instance= song)
    if formsong.is_valid():
        formsong.save()
        return redirect('/show_song')
    return  render(request,"edit_song.html",{'song': song})

def deleteSong(request, id):
    song = Song.objects.get(id=id)
    song.delete()
    return redirect("/show_song")
# ---------------------------------------------------#