from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('client-profile/<pk>/',
         views.view_client_profile,
         name='client_profile'),
    path('client-list/', views.view_client_list, name='client_list'),
    path('create-client-profile/',
         views.create_client_profile,
         name='create_client_profile'),
    path('edit-client-profile/<pk>/',
         views.edit_client_profile,
         name='edit_client_profile'),
    path('remove-client-profile/<pk>/',
         views.remove_client_profile,
         name='remove_client_profile'),
]
urlpatterns += staticfiles_urlpatterns()
