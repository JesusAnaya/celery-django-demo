import celery
from django.contrib.auth.models import User
from .emails import send_welcome_email


class SendWelcomeEmail(celery.Task):
    ignore_result = True

    def run(self, user_id):
        user = User.objects.get(id=user_id)
        send_welcome_email(user)
