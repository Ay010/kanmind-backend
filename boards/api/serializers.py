from rest_framework import serializers
from boards.models import Board
from user_auth.models import User
from tasks.api.serializers import TaskSerializer
from user_auth.api.serializers import UserSerializer


class BoardListSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    tasks_count = serializers.SerializerMethodField()
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)
    tasks_to_do_count = serializers.SerializerMethodField()
    tasks_high_prio_count = serializers.SerializerMethodField()
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Board
        fields = ['id', 'title', 'member_count', 'tasks_count',
                  'tasks_to_do_count', 'tasks_high_prio_count', 'owner_id',
                  'members']

    def get_member_count(self, obj):
        return obj.members.count()

    def get_tasks_count(self, obj):
        return obj.tasks.count()

    def get_tasks_to_do_count(self, obj):
        return obj.tasks.filter(status='to_do').count()

    def get_tasks_high_prio_count(self, obj):
        return obj.tasks.filter(priority='high').count()


class BoardDetailSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Board
        fields = ['id', 'title', 'owner_id', 'members', 'tasks']

    def get_tasks(self, obj):
        return TaskSerializer(obj.tasks.all(), many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['members'] = UserSerializer(
            instance.members.all(), many=True).data
        return representation
