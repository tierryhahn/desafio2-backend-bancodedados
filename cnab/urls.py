from django.urls import path
from .views import ListDetailView

urlpatterns = [
    path('loja/', ListDetailView.as_view()),
]