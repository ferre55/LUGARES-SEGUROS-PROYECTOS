from django.urls import path
from initial import views

urlpatterns = [
    path('Saludos', views.HelloDrf.as_view(), name='index'),
    path('Greetings', views.HelloDrf.as_view(), name='index'),
]