from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.sign_in, name='login')
]
urlpatterns += staticfiles_urlpatterns()
