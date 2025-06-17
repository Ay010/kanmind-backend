from rest_framework.permissions import BasePermission
from tasks.models import Board, Task
from rest_framework.response import Response
from rest_framework import status


class IsMemberInBoard(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            board_id = request.data.get('board')
        else:
            board_id = view.kwargs.get('pk')

        if not Board.objects.filter(id=board_id).exists():
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        return request.user in Board.objects.get(id=board_id).members.all()

    def has_object_permission(self, request, view, obj):
        print("IsMemberInBoard")
        return request.user in obj.board.members.all() or request.user == obj.board.owner_id


class IsCreatorOrBoardOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.created_by or request.user == obj.board.owner_id


class IsTaskBoardMember(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        task_id = view.kwargs.get('pk')

        if not Task.objects.filter(id=task_id).exists():
            return Response(
                {"message": "Task does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not task_id:
            return False
        task = Task.objects.get(id=task_id)
        return request.user in task.board.members.all() or request.user == task.board.owner_id

    def has_object_permission(self, request, view, obj):
        return request.user in obj.board.members.all() or request.user == obj.board.owner_id


class IsCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
