from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.add_cards_view, name='index'),
    path('signup/', views.signup_view, name='signup')
]