from django.urls import path
from . import views

app_name = 'check'

urlpatterns = [
    path('', views.IndexView.as_view(), name='rooms'),
    path('<slug:pk>/', views.RoomView.as_view(), name='form'),
]