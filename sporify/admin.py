from django.contrib import admin

from sporify.models import User, Musician, Song, Playlist

# Register your models here.

admin.site.register(Song)
admin.site.register(Musician)
admin.site.register(User)
admin.site.register(Playlist)