from django.urls import path
from boards.api.views import BoardListCreateView, BoardDetailView, EmailCheckView

urlpatterns = [
    path('boards/', BoardListCreateView.as_view(), name='list-create-board'),
    path('boards/<int:pk>/', BoardDetailView.as_view(), name='board-detail'),
    path('email-check/', EmailCheckView.as_view(), name='email-check'),
]
