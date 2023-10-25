from django.urls import path
from . import views

urlpatterns = [
    path('messages', views.get_messages),
    path('messages/<str:id>', views.get_message)
]