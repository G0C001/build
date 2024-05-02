from django.contrib import admin
from django.urls import path
from my_application import views

urlpatterns = [

    path('', views.user, name='user'),

    path('home/', views.home, name='home'),

    path('admin/', views.admin, name='admin'),


    path('update_mens/',views.update_mens, name='update_mens'),
    path('update_womens/',views.update_womens, name='update_womens'),
    path('update_kides/',views.update_kides, name='update_kides'),

    path('mens/', views.mens, name='mens'),
    path('womens/', views.womens, name='womens'),
    path('kids/', views.kids, name='kids'),

    path('womens_cart/<int:id>/', views.womens_cart, name='womens_cart'),
    
    path('mens_cart/<int:id>/', views.mens_cart, name='mens_cart'),

    path('kids_cart/<int:id>/', views.kids_cart, name='kids_cart'),

    path('addtocart/', views.addtocart, name='addtocart'),

    path('addme/', views.addme, name='addme'),
    
]
