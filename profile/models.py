from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    pic = models.ImageField(upload_to='profiles', null=True, default='profiles/none.png')

    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.user.first_name:
            return f'{self.user.first_name} {self.user.last_name} (@{self.user.username})'
        else:
            return self.user.username


"""
Tying up Profile objects with User objects
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created: return
    Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
