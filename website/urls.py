from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_messages, name="messages"),
    path('messages/create', views.create_message, name="create_message"),
    path('messages/update/<str:id>', views.update_message, name="update_message"),
    path('messages/delete/<str:id>', views.message_delete, name="delete_message"),
    path('messages/<str:id>', views.show_message, name="show_message"),
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="register"),
    path('logout', views.logout_view, name="register"),

]
