from django.shortcuts import render
from django.db.models import Q
from django.views.generic import CreateView, DetailView, ListView
from .forms import ShopForm
from .models import Shop
# Create your views here.

class ShopCreateView(CreateView):
    """Renders create view of a given Shop"""
    form_class = ShopForm
    template_name = 'snippets/form-snippet.html'

    def form_valid(self, form):
        return super(ShopCreateView, self).form_valid(form)


class ShopDetailView(DetailView):
    """Renders the detailed view of a given Shop"""
    queryset = Shop.objects.all()
    model = Shop
    template_name = 'shop/shop_detail.html'




class ShopListView(ListView):
    """Renders the list of shops in a list view"""
    model = Shop
    template_name = 'shop_list.html'
    queryset = Shop.objects.all()
