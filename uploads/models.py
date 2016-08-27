from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core.urlresolvers import reverse_lazy


class UploadImage(models.Model):
    image = models.ImageField(upload_to='images/')

    @property
    def thumbnails(self):
        return ImageThumbnail.objects.filter(original_image=self)

    def __unicode__(self):
        return '{0}'.format(self.image)

    def get_absolute_url(self):
        return reverse_lazy('image-detail', kwargs={'pk': self.pk})


class ImageThumbnail(models.Model):
    original_image = models.ForeignKey(UploadImage)
    thumb = models.ImageField(upload_to='images/thumbnails/')
    size = models.CharField(max_length=10)

    def __unicode__(self):
        return '{0} size {1}'.format(self.original_image, self.size)


@receiver(post_save, sender=UploadImage)
def upload_post_save(sender, instance, **kwargs):
    if settings.USER_CELERY:
        from .tasks import CreateThumbnails
        CreateThumbnails().delay(upload_id=instance.id)
    else:
        from .thumbnails import create_thumbnails
        create_thumbnails(instance)
