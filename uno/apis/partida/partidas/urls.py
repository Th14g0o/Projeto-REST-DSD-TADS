from django.urls import path

from .views import PartidaDetailView, PartidaListView, EntrarPartidaView

urlpatterns = [
    path('partidas/', PartidaListView.as_view()),
    path('partidas/<int:pk>/', PartidaDetailView.as_view()),
    path('partidas/<int:pk>/entrar/', EntrarPartidaView.as_view()),
]