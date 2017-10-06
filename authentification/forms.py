from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all required fields and
    user to retype password.
    """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_conf = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        """Calls User
        """
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        """To check if the email is already registered
        """
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email has already been registered.")
        return email

    def clean_password_conf(self):
        """To make sure the passwords match
        """
        password = self.cleaned_data.get("password")
        password_conf = self.cleaned_data.get("password_conf")
        if password and password_conf and password != password_conf:
            raise forms.ValidationError("Passwords don't match")

    def save(self, commit=True):
        """Saves the provided password in hashed format and saves the user"""
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            print(user.profile)
            user.profile.activate()
        return user
