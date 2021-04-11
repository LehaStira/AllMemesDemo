from django.urls import path
from rest_framework import routers
from .views import MemeViewSet, TagViewSet
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('memes', MemeViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('seraching/<str:data>/', MemeViewSet.as_view({'post':'searching'}))
]