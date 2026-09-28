from django.urls import path
from .views import LoginView, UsuarioListView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view()),
    path('login/', LoginView.as_view()),
]