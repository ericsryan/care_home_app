from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('client-profile/<pk>/',
         views.view_client_profile,
         name='view_client_profile'),
    path('create-client-profile/',
         views.create_client_profile,
         name='create_client_profile'),
    path('edit-client-profile/<pk>/',
         views.edit_client_profile,
         name='edit_client_profile'),
]
urlpatterns += staticfiles_urlpatterns()
