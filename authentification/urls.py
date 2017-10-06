from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import ProfileDetailView

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
]
