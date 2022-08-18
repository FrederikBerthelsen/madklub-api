from rest_framework import serializers
from .models import Madklub
from MyUser.models import MyUser
from djoser.serializers import UserSerializer

class MadklubSerializer(serializers.ModelSerializer):
    participants = UserSerializer(read_only = True, many = True)
    # owner = UserSerializer(read_only = True)
    owner = serializers.PrimaryKeyRelatedField(queryset=MyUser.objects.all())

    class Meta:
        model = Madklub
        fields = ('owner', 'participants', 'date', 'diet', 'active', 'dish')
