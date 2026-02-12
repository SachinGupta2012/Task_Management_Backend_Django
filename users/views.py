from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from .models import User, OTP
from .serializers import RequestOTPSerializer, VerifyOTPSerializer

from drf_spectacular.utils import extend_schema
from activity.utils import log_activity
from .throttles import OTPThrottle



class RequestOTPView(APIView):
    serializer_class = RequestOTPSerializer
    permission_classes = []
    throttle_classes = [OTPThrottle]
    @extend_schema(request=RequestOTPSerializer)
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=request.data["email"])
        log_activity(user, "OTP_REQUEST", request)

        return Response({"message": "OTP sent"}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    permission_classes = []

    @extend_schema(request=VerifyOTPSerializer)
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        try:
            user = User.objects.get(email=email)
            otp = OTP.objects.filter(user=user, code=code).latest('created_at')

            if not otp.is_valid():
                return Response({"error": "OTP expired"}, status=400)

            refresh = RefreshToken.for_user(user)
            log_activity(user, "LOGIN_SUCCESS", request)

            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })

        except:
            return Response({"error": "Invalid OTP"}, status=400)

