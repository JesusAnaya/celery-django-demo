from django.contrib import admin
from .models import UploadImage, ImageThumbnail


admin.site.register(UploadImage)
admin.site.register(ImageThumbnail)
