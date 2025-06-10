from django.urls import path
from tasks.api.views import TaskCreateView, TaskDetailView, AssignedToMeView, ReviewingListView, TaskCommentView, DeleteTaskCommentView

urlpatterns = [
    path('', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/comments/', TaskCommentView.as_view(), name='task_comment'),
    path('<int:pk>/comments/<int:comment_id>/',
         DeleteTaskCommentView.as_view(), name='task_comment_detail'),
    path('assigned-to-me/', AssignedToMeView.as_view(), name='assigned_to_me'),
    path('reviewing/', ReviewingListView.as_view(), name='reviewing'),
]
