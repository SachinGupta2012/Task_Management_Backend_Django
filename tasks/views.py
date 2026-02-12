from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.exceptions import PermissionDenied
from .models import Task
from .serializers import TaskSerializer
from activity.utils import log_activity


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        # Users can only access their own tasks
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)

        log_activity(
            user=self.request.user,
            action="TASK_CREATE",
            request=self.request,
            metadata={"task_id": task.id}
        )

    def perform_update(self, serializer):
        task = serializer.save()

        log_activity(
            user=self.request.user,
            action="TASK_UPDATE",
            request=self.request,
            metadata={"task_id": task.id}
        )

    def perform_destroy(self, instance):
        log_activity(
            user=self.request.user,
            action="TASK_DELETE",
            request=self.request,
            metadata={"task_id": instance.id}
        )

        instance.delete()
