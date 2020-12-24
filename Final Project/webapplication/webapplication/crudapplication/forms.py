from django import forms
from crudapplication.models import User, Playlist, Friends, Song 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = "__all__"

class FriendsForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = "__all__"

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"