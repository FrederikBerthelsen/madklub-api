from rest_framework import generics, permissions, response
from MyUser.serializers import MyUserStaffSerializer

# Create your views here.
class GetStaffStatusView(generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated)

    def get(self, request):
        user = request.user
        serializer = MyUserStaffSerializer(user)
        return response.Response(serializer.data)

