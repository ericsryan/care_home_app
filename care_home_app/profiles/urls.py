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
    path('doctor-profile/<pk>/',
         views.view_doctor_profile,
         name='doctor_profile'),
    path('doctor-list/', views.view_doctor_list, name='doctor_list'),
    path('create-doctor-profile/',
         views.create_doctor_profile,
         name='create_doctor_profile'),
    path('edit-doctor-profile/<pk>/',
         views.edit_doctor_profile,
         name='edit_doctor_profile'),
]
urlpatterns += staticfiles_urlpatterns()
