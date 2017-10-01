from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse
# Create your models here.


def upload_location(instance, filename):
    """Returns the path to upload the file to"""
    return "{}/{}".format(instance.id, filename)


class Shop(models.Model):
    """Creates Coffee Shop model with
    name, location, description, image field, overall rating, and recent reviews attributes
    """
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True,
                              width_field='width_field', height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        """Returns a string represetntation of the Shop
        @:type self: Shop
        @:rtype: str
        """
        return self.name

    def get_absolute_url(self):
        """Gives the url of the Shop model
        :rtype: url
        """
        return reverse('shop:detail', kwargs={'slug': self.slug})


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    """Uses signals to create slug for model if slugfield is empty"""
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Shop)
