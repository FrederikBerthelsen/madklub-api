from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from MyUser.models import MyUser
import datetime
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import SchemaSerializer
from .models import Schema
from .permissions import SchemaPermissions

class SchemaView(APIView):
    permission_classes = (SchemaPermissions,)

    def get(self, request):
        today = datetime.date.today()
        week = today.isocalendar().week
        schemas = Schema.objects.filter()
        serializer = SchemaSerializer(schemas, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = SchemaSerializer(data=data, many = True)
        if serializer.is_valid():
            input_data = serializer.validated_data
            for i in input_data:
                user_ids = i.get('user_ids')
                for id in user_ids:
                    if not MyUser.objects.filter(id = id).exists():
                        return Response("User does not exist", status = status.HTTP_400_BAD_REQUEST)
            ret = []
            for i in input_data:
                week = i.get('week')
                user_ids = i.get('user_ids')

                if Schema.objects.filter(week = week).count() > 0:
                    schema = Schema.objects.get(week = week)
                else:
                    schema = Schema.objects.create(week = week)
                schema.users.set(user_ids)
                schema.save()
                ret.append(SchemaSerializer(schema).data)

            return Response(ret, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

