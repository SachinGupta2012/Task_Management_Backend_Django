from .models import ActivityLog


def log_activity(user, action, request, metadata=None):
    ip = request.META.get("REMOTE_ADDR")

    ActivityLog.objects.create(
        user=user,
        action=action,
        ip_address=ip,
        metadata=metadata or {}
    )
