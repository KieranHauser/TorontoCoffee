from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .utils import code_generator
# Create your models here.

User = settings.AUTH_USER_MODEL


class ProfileManager(models.Manager):
    """Profile manager
    """
    def toggle_follow(self, requested_user, username_to_toggle):
        """Toggles follow on and off
        """
        profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
        user = requested_user
        is_following = False
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            is_following = True
        return profile_, is_following


class Profile(models.Model):
    """The Profile model where users can vote, favourite and review coffeeshops.
    """
    user = models.OneToOneField(User)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    objects = ProfileManager()

    def __str__(self):
        """Returns string representation of the user
        """
        return self.user.username

    def send_activation_email(self):
        """Sends activation email to the email the user entered with an activationkey
        """
        self.save()
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            html_message = f'Activate your account here {path_}'
            print(f'{path_}')
            print(html_message)
            sent_mail = False
            return sent_mail

    def get_absolute_url(self):
        """Gives the url of the Profile model
        :rtype: url
        """
        return reverse('authentification:detail', kwargs={'user': self.user})

    def activate(self):
        """Activates account
        """
        if not self.activated:
            qs = Profile.objects.all()
            profile = qs.order_by('-timestamp').first()
            user_ = profile.user
            user_.is_active = True
            user_.save()
            profile.activated = True
            profile.activation_key = None


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    """Post save with signals to create profile properly
    """
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
        default_user_profile = Profile.objects.all().first() # user__username=
        default_user_profile.followers.add(instance)
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)
