from django.urls import path
from . import views

urlpatterns = [
    path('my-first-view', views.first_view, name='my-first-view')
]