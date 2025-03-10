from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/edit/<int:product_id>/' , views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/' , views.delete_product, name='delete_product'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
 


]