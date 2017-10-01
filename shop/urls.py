from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import ShopCreateView, ShopDetailView, ShopListView

urlpatterns = [
    url(r'^create/', ShopCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ShopDetailView.as_view(), name='detail'),
    url(r'$', ShopListView.as_view(), name='list'),
]
