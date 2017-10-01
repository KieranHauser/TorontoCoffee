from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from .utils import code_generator
# Create your models here.

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    """The Profile model where users can vote, favourite and review coffeeshops.
    """
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        """Returns string representation of the user
        """
        return self.user.username


