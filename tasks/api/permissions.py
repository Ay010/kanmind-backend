from rest_framework.permissions import BasePermission
from tasks.models import Board, Task


class IsMemberInBoard(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.board.members.all() or request.user == obj.board.owner_id


class IsCreatorOrBoardOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.created_by or request.user == obj.board.owner_id


class IsTaskBoardMember(BasePermission):
    def has_permission(self, request, view):
        task_id = view.kwargs.get('pk')
        if not task_id:
            return False
        task = Task.objects.get(id=task_id)
        return request.user in task.board.members.all() or request.user == task.board.owner_id

    def has_object_permission(self, request, view, obj):
        return request.user in obj.board.members.all() or request.user == obj.board.owner_id


class IsCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
