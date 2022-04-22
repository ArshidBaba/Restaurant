from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuListCreateAPIView.as_view()),
    path('<int:pk>/', views.MenuDetailAPIView.as_view())
]