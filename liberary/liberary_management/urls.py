from django.urls import path
from . import views

urlpatterns = [
    # -------------------- Home --------------------
    path('', views.HomeView.as_view(), name='home'),

    # -------------------- Books --------------------
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    # -------------------- Members --------------------
    path('members/', views.MemberListView.as_view(), name='member_list'),
    path('members/create/', views.MemberCreateView.as_view(), name='member_create'),
    path('members/<int:pk>/update/', views.MemberUpdateView.as_view(), name='member_update'),
    path('members/<int:pk>/delete/', views.MemberDeleteView.as_view(), name='member_delete'),


    # -------------------- Loans --------------------
    path('loans/', views.LoanListView.as_view(), name='loan_list'),
    path('loans/create/', views.LoanCreateView.as_view(), name='loan_create'),
    path('loans/<int:pk>/return/', views.LoanReturnView.as_view(), name='loan_return'),
    path('loans/<int:pk>/update/', views.LoanUpdateView.as_view(), name='loan_update'),
    path('loans/<int:pk>/delete/', views.LoanDeleteView.as_view(), name='loan_delete'),

    # -------------------- Fines --------------------
    path('fines/', views.FineListView.as_view(), name='fine_list'),
    path('fines/<int:pk>/delete/', views.FineDeleteView.as_view(), name='fine_delete'),
]
