from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'pdf_filler'
urlpatterns = [
    path('fill-LIC624/<client_pk>', views.fill_LIC624, name='fill_LIC624'),
]
urlpatterns += staticfiles_urlpatterns()
