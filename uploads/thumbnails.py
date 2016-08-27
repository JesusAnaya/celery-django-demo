from django.core.files.base import ContentFile
from sorl.thumbnail import get_thumbnail
from .models import ImageThumbnail
import time


def create_thumbnails(upload):
    thumb_sizes = (
        (150, 150),
        (100, 100),
        (50, 50),
    )

    for thumb_size in thumb_sizes:
        size = "{0}x{1}".format(*thumb_size)
        resized = get_thumbnail(upload.image, size, crop='center', quality=99)

        img = ImageThumbnail(original_image=upload, size=size)
        img.thumb = ContentFile(resized.read(), resized.name)

        time.sleep(1)
        img.save()
