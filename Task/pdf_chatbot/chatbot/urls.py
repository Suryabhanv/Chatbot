from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_pdf, name='upload'),
    path('chat/', views.chat_with_pdf, name='chat'),
]
