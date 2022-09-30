from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

ADMIN = 'Admin'
CLIENT = 'Client'

ROLE = (
    (ADMIN, 'Admin'),
    (CLIENT, 'Client')
)


class User(AbstractUser):
    role = models.CharField(max_length=127, choices=ROLE, default=CLIENT)


class UserAdmin (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_admin')


class UserClient (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_client')


@receiver(post_save, sender=User)
def create_users(sender, instance, created, **kwargs):
    if created:
        if instance.role == ADMIN:
            UserAdmin.objects.create(user=instance)
        elif instance.role == CLIENT:
            UserClient.objects.create(user=instance)


