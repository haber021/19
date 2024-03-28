from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.index.as_view(), name='index'),  # Use index.as_view() instead of index
]
