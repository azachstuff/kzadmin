from django.contrib import admin

from .models import Album, Image, Upload
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
  class Meta:
    model = Album

  list_display = ('name', 'desc')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Image)
admin.site.register(Upload)