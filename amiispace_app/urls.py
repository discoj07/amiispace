from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup_view, name='signup')
]