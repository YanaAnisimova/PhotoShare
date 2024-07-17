from django.contrib import admin

from .models import Photo, PhotoRating, Tag


admin.site.register(Photo)
admin.site.register(PhotoRating)
admin.site.register(Tag)

