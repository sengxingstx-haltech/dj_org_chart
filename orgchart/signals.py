import os

from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from .models import Employee


@receiver(pre_save, sender=Employee)
def handle_avatar_update(sender, instance, **kwargs):
    """Delete the old avatar file when the avatar is updated."""
    print("Triggered signals....")
    # Check if the avatar field has changed
    if instance.avatar:
        try:
            # Get the old instance to compare the avatar
            old_instance = Employee.objects.get(id=instance.id)
            if old_instance.avatar and old_instance.avatar != instance.avatar:
                if os.path.isfile(old_instance.avatar.path):
                    os.remove(old_instance.avatar.path)
        except Employee.DoesNotExist:
            pass


@receiver(pre_delete, sender=Employee)
def handle_avatar_delete(sender, instance, **kwargs):
    """Delete the avatar file when the Employee instance is deleted."""
    if instance.avatar:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)
