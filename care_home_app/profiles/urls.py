from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('create-client-profile/',
         views.create_client_profile,
         name='create_client_profile'),
]
urlpatterns += staticfiles_urlpatterns()
