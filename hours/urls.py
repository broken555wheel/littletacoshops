from django.urls import path
from . import views
# from .views import hours

urlpatterns = [
    path('hours.html', views.hours, name='hours'),
]