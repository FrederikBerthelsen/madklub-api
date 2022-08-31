from rest_framework import serializers
from djoser.conf import settings

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="key")
    is_staff = serializers.BooleanField(source="user.is_staff", read_only=True, default=False)
    email = serializers.CharField(source="user.email", read_only=True, default=False)

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("auth_token", "is_staff", "email")
