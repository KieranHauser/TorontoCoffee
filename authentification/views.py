from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, View
from shop.models import Shop
from .models import Profile
from .forms import RegisterForm

User = get_user_model()


def activate_user_view(request, code=None, *args, **kwargs):
    """View to activate user
    """
    # if code:
    #     qs = Profile.objects.filter(activation_key=code)
    #     if qs.exists() and qs.count() == 1:
    #         profile = qs.first()
    #         if not profile.activated:
    #             user_ = profile.user
    #             user_.is_active = True
    #             user_.save()
    #             profile.activated = True
    #             profile.activation_key = None
    #             return redirect("/login")
    qs = Profile.objects.all()
    profile = qs.first().order_by('-timestamp')
    user_ = profile.user
    user_.is_active = True
    user_.save()
    profile.activated = True
    profile.activation_key = None
    return redirect("/login")


class RegisterView(CreateView):
    """Makes view to register user
    """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        """Checks if user is authenticated
        """
        if self.request.user.is_authenticated():
            return redirect("/login")
        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class ProfileFollowToggle(LoginRequiredMixin, View):
    """Class to toggle the follow if user is following the person and untoggle as well
    Inherits from generic view class and check that the user is logged in
    """
    def post(self, request, *args, **kwargs):
        """Toggles follow for user
        """
        username_to_toggle = request.POST.get("username")
        profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle)
        return redirect(f"/u/{profile_.user.username}")


class ProfileDetailView(DetailView):
    """Provides a detail view of the selected profile
    """
    template_name = 'authentification/authentification_detail.html'

    def get_object(self):
        """Gets User Object
        """
        username = self.kwargs["username"]
        if username is None:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        """Returns context data for DetailView
        :type args: args
        :type kwargs: kwargs
        :rtype: dict
        """
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['user']
        # if user.profile in self.request.user.is_following.all():
        #     is_following = True
        # else:
        #     is_following = False
        # context['is_following'] = is_following
        return context
