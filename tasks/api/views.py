from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from tasks.models import Task, TaskComment
from tasks.api.serializers import TaskSerializer, TaskCommentSerializer, TaskDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView
from tasks.api.permissions import IsMemberInBoard, IsCreatorOrBoardOwner, IsTaskBoardMember, IsCreator
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsMemberInBoard]

    def get_queryset(self):
        return Task.objects.all()


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsCreatorOrBoardOwner()]
        return [IsMemberInBoard()]

    def get_queryset(self):
        return Task.objects.all()

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response(
            {"message": f"task successfully deleted."},
            status=status.HTTP_204_NO_CONTENT
        )


class AssignedToMeView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class ReviewingListView(ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(reviewer_id=self.request.user.id)


class TaskCommentView(ListCreateAPIView):
    serializer_class = TaskCommentSerializer
    permission_classes = [IsTaskBoardMember]

    def get_queryset(self):
        if not Task.objects.filter(id=self.kwargs['pk']).exists():
            raise Http404(
                f"Task does not exist.")
        return TaskComment.objects.filter(task_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        if not Task.objects.filter(id=self.kwargs['pk']).exists():
            raise Http404(
                f"Task does not exist.")
        serializer.save(
            author=self.request.user,
            task_id=self.kwargs['pk']
        )


class DeleteTaskCommentView(DestroyAPIView):
    serializer_class = TaskCommentSerializer
    permission_classes = [IsCreator]

    def get_queryset(self):
        queryset = TaskComment.objects.filter(
            task_id=self.kwargs['pk'],
            id=self.kwargs['comment_id']
        )
        return queryset

    def get_object(self):

        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            raise Http404(
                f"comment {self.kwargs['comment_id']} does not exist in task {self.kwargs['pk']}")
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response(
            {"message": f"comment successfully deleted."},
            status=status.HTTP_204_NO_CONTENT
        )
