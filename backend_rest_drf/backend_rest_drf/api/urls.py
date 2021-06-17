from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path

router = DefaultRouter()
router.register(r'store', StoreViewSet, basename='store')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'menu', MenuViewSet, basename='menu')

urlpatterns = [
    re_path(r'^v(?P<version>(1))/', include(router.urls)),
]
