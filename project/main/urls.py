from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('carts/', views.CartListView.as_view()),
    path('cart/', views.CartDetailedView.as_view())
]
