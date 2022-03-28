from .views import RegisterAPI, LoginAPI, ItemAPIView
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('items/', ItemAPIView.as_view(), name='items'),
]
