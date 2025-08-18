from main.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actors/', ActorsAPIView.as_view()),
    path('actors/<int:pk>/', ActorRetrieveUpdateAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateAPIView.as_view()),

    path('', include(router.urls))
]
