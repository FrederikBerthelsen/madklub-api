from rest_framework import serializers
from .models import Schema
from djoser.serializers import UserSerializer

class SchemaSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only = True, many = True)
    user_ids = serializers.ListField(
            child = serializers.IntegerField(),
            write_only = True
        )

    class Meta:
        model = Schema
        fields = ('week', 'users', 'user_ids')

    # def create(self, validated_data):
    #     # print("Entered create")
    #     # print(validated_data.get('users'))
    #     users_data = validated_data.pop('users')
    #     users = MyUser.objects.filter(id__in=users_data)
    #     schema = Schema.objects.create(week=validated_data.week, users=users)
    #
    #     # answer, created = Schema.objects.update_or_create(
    #     #     week=validated_data.get('week', 1),
    #     #     defaults={'users', validated_data.get('users', [])}
    #     # )
    #     return schema
    #
    # def update(self, instance, validated_data):
    #     print("Entered UPDATE")
    #     users_data = validated_data.pop('users')
    #     users = MyUser.objects.filter(id__in=users_data)
    #     instance.users.clear()
    #     instance.users.add(*users)
    #     instance.saver()
    #     return instance
