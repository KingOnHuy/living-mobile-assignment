from .views import StoreViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path

router = DefaultRouter()
router.register(r'store', StoreViewSet, basename='store')

urlpatterns = [
    re_path(r'^v(?P<version>(1))/', include(router.urls)),
]
