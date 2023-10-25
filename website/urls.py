from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_messages, name="messages"),
    path('messages/create', views.create_message, name="create_message"),
    path('messages/update/<str:id>', views.update_message, name="update_message"),
    path('messages/delete/<str:id>', views.message_delete, name="delete_message"),
    path('messages/response/add/<str:id>', views.add_response, name="response_message"),
    path('messages/response/delete/<str:id>', views.response_delete, name="delete_response"),
    path('messages/response/update/<str:id>', views.response_update, name="update_response"),
    path('messages/<str:id>', views.show_message, name="show_message"),
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),

]
