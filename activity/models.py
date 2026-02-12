from django.db import models
from django.conf import settings


class ActivityLog(models.Model):
    ACTION_CHOICES = (
        ("OTP_REQUEST", "OTP Request"),
        ("LOGIN_SUCCESS", "Login Success"),
        ("TASK_CREATE", "Task Create"),
        ("TASK_UPDATE", "Task Update"),
        ("TASK_DELETE", "Task Delete"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action}"
