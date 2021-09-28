from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'pdf_filler'
urlpatterns = [
    path('fill-pdf/', views.fill_pdf, name='fill_pdf'),
]
urlpatterns += staticfiles_urlpatterns()
