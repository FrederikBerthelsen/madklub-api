from rest_framework import serializers
from .models import Madklub, MadklubParticipant #, VeganParticipants, VegetarianParticipants, MeatParticipants
from MyUser.models import MyUser
from djoser.serializers import UserSerializer

class ParticipantSerializer(serializers.ModelSerializer):
    participant = UserSerializer(read_only=True)
    
    class Meta:
        model = MadklubParticipant
        fields = ('participant', 'diet', 'guests')

class MadklubSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    participants = ParticipantSerializer(read_only=True, source="madklubparticipant_set", many=True)

    class Meta:
        model = Madklub
        fields = "__all__"
        depth = 1
