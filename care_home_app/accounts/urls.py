from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('view/', views.view_account, name='view'),
    path('edit/', views.edit_account, name='edit'),
]
urlpatterns += staticfiles_urlpatterns()
