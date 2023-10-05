from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


app_name = 'items'
urlpatterns = [


    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('lost_items/', views.lost_items_list, name='lost_items_list'),
    path('add_lost_item/', views.add_lost_item, name='add_lost_item'),
    path('found_items/', views.found_items_list, name='found_items_list'),
    path('claimed_items/', views.claimed_items_list, name='claimed_items_list'),
    path('add_found_item/', views.add_found_item, name='add_found_item'),
    path('add_claimed_item/', views.add_claimed_item, name='add_claimed_item'),
    
    

  ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
