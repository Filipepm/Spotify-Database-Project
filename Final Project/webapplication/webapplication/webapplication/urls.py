"""webapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crudapplication import views
from register import views as registerV

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', registerV.register, name = "register"),
    path('', include("django.contrib.auth.urls")),
    
    path('userr', views.userr),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),

    path('playlistt', views.playlistt),
    path('show_playlist', views.showPlaylist),
    path('editPlaylist/<int:id>', views.editPlaylist),
    path('updatePlaylist/<int:id>', views.updatePlaylist),
    path('deletePlaylist/<int:id>', views.deletePlaylist),

    path('friendd', views.friendd),
    path('show_friend', views.showFriend),
    path('editFriend/<int:id>', views.editFriend),
    path('updateFriend/<int:id>', views.updateFriend),
    path('deleteFriend/<int:id>', views.deleteFriend),

    path('songg', views.songg),
    path('show_song', views.showSong),
    path('editSong/<int:id>', views.editSong),
    path('updateSong/<int:id>', views.updateSong),
    path('deleteSong/<int:id>', views.deleteSong),
]
