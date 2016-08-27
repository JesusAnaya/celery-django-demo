from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .emails import send_welcome_email
from .tasks import SendWelcomeEmail


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    if instance.email:
        if settings.USER_CELERY:
            SendWelcomeEmail().delay(user_id=instance.id)
        else:
            send_welcome_email(instance)
