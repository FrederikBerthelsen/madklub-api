from rest_framework.decorators import permission_classes, action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from MyUser.models import MyUser
from datetime import date

from .serializers import MadklubSerializer
from .models import Madklub, MadklubParticipant
from .permissions import MadklubPermissions

class MadklubViewSet(ModelViewSet):
    serializer_class = MadklubSerializer
    queryset = Madklub.objects.filter(date__gte=date.today())
    permission_classes = [MadklubPermissions]

    def perform_create(self, serializer, user, data):
        if 'guests' in data:
            guests = data['guests']
        else:
            guests = 0
        diet = user.diet
        madklub = serializer.save(owner=user, participants=[])
        MadklubParticipant.objects.create(participant=user, madklub=madklub, diet=diet, guests=guests)
        return madklub

    def create(self, request):
        data = request.data
        user = request.user
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            if user.diet in data['diet']:
                madklub = self.perform_create(serializer, user, data)
                return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
            else:
                return Response([{'diet': "Your diet is not represented in the available diets"}], status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status = status.HTTP_200_OK)

    def partial_update(self, request, pk):
        data = request.data
        user = request.user
        if Madklub.objects.filter(id = pk).count() > 0:
            madklub = Madklub.objects.get(id = pk)
            oldDate = madklub.date
            if madklub.owner != request.user:
                return Response([{'madklub': 'You are not the owner of the madklub'}], status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(madklub, data=data)
            if serializer.is_valid():
                if user.diet not in data['diet']:
                    return Response([{'diet': 'Your diet is not represented in the available diets'}], status=status.HTTP_400_BAD_REQUEST)
                madklub = serializer.save()
                if oldDate != madklub.date:
                    MadklubParticipant.objects.filter(madklub=madklub).exclude(participant=user).delete()
                return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        print("Entered Delete")
        user = request.user
        if Madklub.objects.filter(id = pk).count() > 0:
            madklub = Madklub.objects.get(id = pk)
            if madklub.owner != user:
                return Response([{'madklub': 'You are not the owner of the madklub'}], status=status.HTTP_400_BAD_REQUEST)
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_400_BAD_REQUEST)


    @action(["post"], permission_classes=[IsAuthenticated], detail=False)
    def join(self, request):
        data = request.data
        if "date" not in data or "diet" not in data:
            return Response("Wrong input given", status=status.HTTP_200_OK)
        date = data['date']
        diet = data['diet']
        if 'guests' in data:
            guests = data['guests']
        else:
            guests = 0
        user = request.user
        if Madklub.objects.filter(date = date).count() > 0:
            madklub = Madklub.objects.get(date = date)
            if MadklubParticipant.objects.filter(participant=user, madklub=madklub).count() > 0:
                return Response([{'madklub': 'You have already joined this madklub'}], status=HTTP_400_BAD_REQUEST)
            if diet in madklub.diet:
                MadklubParticipant.objects.create(participant=user, madklub=madklub, diet=diet, guests=guests)
                return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
            else:
                return Response([{'diet': 'Your chosen diet is not represented in the available diets'}], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_200_OK)

    @action(["post"], permission_classes=[IsAuthenticated], detail=False)
    def leave(self, request):
        data = request.data
        if "date" not in data:
            return Response('Wrong data sent', status = status.HTTP_400_BAD_REQUEST)
        user = request.user
        date = data['date']
        if Madklub.objects.filter(date = date).count() > 0:
            madklub = Madklub.objects.get(date = date)
            try:
                MadklubParticipant.objects.get(participant=user, madklub=madklub).delete()
                return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
            except:
                return Response([{'madklub': 'You are not apart of this madklub'}], status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_400_BAD_REQUEST)

    @action(["post"], permission_classes=[IsAuthenticated], detail=False)
    def updateParticipant(self, request):
        data = request.data
        if "date" not in data:
            return Response('Wrong data sent', status = status.HTTP_400_BAD_REQUEST)
        date = data['date']
        user = request.user
        if Madklub.objects.filter(date = date).count() > 0:
            madklub = Madklub.objects.get(date = date)
            if not (MadklubParticipant.objects.filter(participant=user, madklub=madklub)):
                return Response([{'madklub': 'You are not apart of this madklub'}], status=status.HTTP_400_BAD_REQUEST)
            else:
                participant = MadklubParticipant.objects.get(participant=user, madklub=madklub)
                if "guests" in data:
                    participant.guests = data['guests']
                if "diet" in data and data['diet'] in madklub.diet:
                    participant.diet = data['diet']
                else:
                    return Response([{'diet': 'No diet given or diet not in available diets'}], status=status.HTTP_400_BAD_REQUEST)
                participant.save(update_fields=['guests', 'diet'])
                return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_400_BAD_REQUEST)

    @action(["post"],permission_classes=[IsAuthenticated], detail=False)
    def activate(self, request):
        data = request.data
        if "date" not in data:
            return Response('Wrong data sent', status = status.HTTP_400_BAD_REQUEST)
        date = data['date']
        user = request.user
        if Madklub.objects.filter(date = date).count() > 0:
            madklub = Madklub.objects.get(date = date)
            if madklub.owner != user:
                return Response([{'madklub': 'You are not the owner of the madklub'}], status=status.HTTP_400_BAD_REQUEST)
            madklub.active = True
            madklub.save(update_fields=['active'])
            return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_400_BAD_REQUEST)

    @action(["post"],permission_classes=[IsAuthenticated], detail=False)
    def deactivate(self, request):
        data = request.data
        if "date" not in data:
            return Response('Wrong data sent', status = status.HTTP_400_BAD_REQUEST)
        date = data['date']
        user = request.user
        if Madklub.objects.filter(date = date).count() > 0:
            madklub = Madklub.objects.get(date = date)
            if madklub.owner != user:
                return Response([{'madklub': 'You are not the owner of the madklub'}], status=status.HTTP_400_BAD_REQUEST)
            madklub.active = False
            madklub.save(update_fields=['active'])
            return Response(MadklubSerializer(madklub).data, status=status.HTTP_200_OK)
        else:
            return Response([{'madklub': 'The madklub does not exist'}], status=status.HTTP_400_BAD_REQUEST)

