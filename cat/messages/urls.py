from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.messages_page, name='messages'),
    path('send/', views.send_message, name='send_message'),
]