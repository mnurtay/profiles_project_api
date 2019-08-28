from django.urls import path, include

from . import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]