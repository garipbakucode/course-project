from django.urls import path
from .views import contact


urlpatterns = [
    path('elaqe/', contact, name='contact'),
]
