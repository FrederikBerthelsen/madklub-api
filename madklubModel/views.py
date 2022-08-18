from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from MyUser.models import MyUser

from .serializers import MadklubSerializer
from .models import Madklub
from .permissions import MadklubPermissions

# class MadklubView(APIView):
#     permission_classes = (MadklubPermissions,)
#
#     def get(self, request):
#         madklubs = Madklub.objects.all()
#         serializer = MadklubSerializer(madklubs, many = True)
#
#         return Response(serializer.data)
#     
#     def post(self, request):

class MadklubViewSet(ModelViewSet):
    serializer_class = MadklubSerializer
    queryset = Madklub.objects.all()
    permission_classes = [MadklubPermissions]


