from django.urls import path
from .views import GroceryListView, GroceryCreateView, GroceryUpdateView, GroceryDeleteView

urlpatterns = [
    path("", GroceryListView.as_view(), name='grocery_list'),
    path("create/", GroceryCreateView.as_view(), name='grocery_create'),
    path("update/<int:pk>/", GroceryUpdateView.as_view(), name='grocery_update'),
    path("delete/<int:pk>/", GroceryDeleteView.as_view(), name='grocery_delete'),
]