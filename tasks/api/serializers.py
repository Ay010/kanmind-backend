from rest_framework import serializers
from tasks.models import Task, TaskComment
from user_auth.models import User
from user_auth.api.serializers import UserSerializer
from boards.models import Board


class TaskCommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = TaskComment
        fields = ['id', 'created_at', 'author', 'content']

    def get_author(self, obj):
        return obj.author.fullname

    def save(self, **kwargs):
        kwargs['author'] = self.context['request'].user
        return super().save(**kwargs)


class TaskSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    assignee = UserSerializer(read_only=True, required=False, allow_null=True)
    reviewer = UserSerializer(read_only=True)
    assignee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assignee',
        write_only=True,
        required=False,
        allow_null=True
    )
    reviewer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='reviewer',
        write_only=True
    )
    board = serializers.PrimaryKeyRelatedField(
        queryset=Board.objects.all()
    )

    class Meta:
        model = Task
        fields = ['id', 'board', 'title', 'description', 'status',
                  'priority', 'assignee', 'reviewer', 'assignee_id', 'reviewer_id',
                  'due_date', 'comments_count']
        read_only_fields = ['board']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def status_validation(self, status):
        if status not in ['to-do', 'in-progress', 'review', 'done']:
            raise serializers.ValidationError("Invalid status")
        return status

    def priority_validation(self, priority):
        if priority not in ['low', 'medium', 'high']:
            raise serializers.ValidationError("Invalid priority")
        return priority

    def board_validation(self, board):
        if not board:
            raise serializers.ValidationError("Board is required")

        user = self.context['request'].user
        if user not in board.members.all() and user != board.owner_id:
            raise serializers.ValidationError(
                "You must be a member of the board to create a task")
        return board

    def save(self, **kwargs):
        kwargs['created_by'] = self.context['request'].user
        return super().save(**kwargs)


class TaskDetailSerializer(TaskSerializer):
    board = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    def board_validation(self, board):
        if board:
            raise serializers.ValidationError("You can't change the board")
        return board
