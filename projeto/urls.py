
from django.contrib import admin
from django.urls import path, include
from core.views import ItemsViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('items', ItemsViewsSet, basename='Items')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]