from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import GroceryItem
from django.urls import reverse_lazy

class GroceryListView(ListView):
    model = GroceryItem
    template_name = 'grocery_list/list.html'
    context_object_name = 'items'

class GroceryCreateView(CreateView):
    model = GroceryItem
    template_name = 'grocery_list/create.html'
    fields = [
        'item_name', 'quantity', 'unit', 'price_per_unit', 'total_price',
        'is_purchased', 'purchase_date', 'expiry_date', 'store_name',
        'created_by', 'email', 'category'
    ]
    success_url = reverse_lazy("grocery_list")

class GroceryUpdateView(UpdateView):
    model = GroceryItem
    template_name = 'grocery_list/update.html'
    fields = [
        'item_name', 'quantity', 'unit', 'price_per_unit', 'total_price',
        'is_purchased', 'purchase_date', 'expiry_date', 'store_name',
        'created_by', 'email', 'category'
    ]
    success_url = reverse_lazy("grocery_list")

class GroceryDeleteView(DeleteView):
    model = GroceryItem
    template_name = 'grocery_list/delete.html'
    success_url = reverse_lazy("grocery_list")

