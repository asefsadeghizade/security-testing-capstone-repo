from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("menu-items/", views.MenuItemView.as_view(), name="menu-items"),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view(), name="single-menu-item"),
    #path("message/", views.msg, name="auth-msg"),
    path("index/", views.index, name="home"),
    path("booking/", views.Booking.as_view(), name="booking"),
    path('api-token-auth/', obtain_auth_token),
]
