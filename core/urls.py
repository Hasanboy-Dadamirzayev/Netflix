from main.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('actors/', ActorsAPIView.as_view()),
    path('actors/<int:pk>/', ActorRetrieveUpdateAPIView.as_view()),
    path('movies/', MoviesAPIView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveUpdateAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateAPIView.as_view()),
]
