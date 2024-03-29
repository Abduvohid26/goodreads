from django.db.models.signals import post_save
from django.dispatch import receiver
from django_email_verification import send_email

from users.models import User


# @receiver(post_save, sender=User)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         send_email(
#             'Welcome to GoogReads Clone',
#             f' Hi {instance.username}. Welcome to GoogReads Clone ',
#             'abdujalilov2629@gmail.com',
#             [instance.email]
#         )















