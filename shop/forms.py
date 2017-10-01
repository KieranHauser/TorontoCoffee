from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    """Form to create new Shop model
    """
    class Meta:
        """Uses Shop model and forms.ModelForm to create Shop form.
        """
        model = Shop
        fields = ['name',
                  'location',
                  'description',
                  'image']
