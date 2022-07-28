from rest_framework.serializers import ModelSerializer

from .models import MyUser

class MyUserStaffSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('is_staff',)