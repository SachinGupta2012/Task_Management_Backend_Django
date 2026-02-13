from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta
from .models import User, OTP
from django.core.mail import send_mail
from django.conf import settings


class RequestOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        email = validated_data['email']
        user, _ = User.objects.get_or_create(email=email)

        code = OTP.generate_otp()

        OTP.objects.create(
            user=user,
            code=code,
            expires_at=timezone.now() + timedelta(minutes=5)
        )

        send_mail(
        subject="Your Task Manager OTP",
        message=f"Your OTP is {code}. It expires in 5 minutes.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )  # Replace with real email later

        return user


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)
