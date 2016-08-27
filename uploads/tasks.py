import celery
from .models import UploadImage
from .thumbnails import create_thumbnails


class CreateThumbnails(celery.Task):
    ignore_result = True

    def run(self, upload_id):
        upload = UploadImage.objects.get(id=upload_id)
        create_thumbnails(upload)
