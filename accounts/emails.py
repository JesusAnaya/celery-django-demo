from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
import logging
import time

logger = logging.getLogger(__name__)


def send_welcome_email(user):
    subject = "Welcome to the Celery demo"
    to = [user.email]
    from_email = settings.EMAIL_HOST_USER

    context = {
        'user': user
    }

    message = get_template('emails/welcome.html').render(context)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'

    try:
        time.sleep(2)
        msg.send()
    except Exception as e:
        logger.error('SendWelcomeEmail: {0}'.format(e))
