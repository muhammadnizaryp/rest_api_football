from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from footballplayer.models import FootballPlayer
from footballplayer.serializers import FootballPlayerSerializer

# Create your views here.

@api_view(['GET'])
def footballplayer_list(request):
    if request.method == 'GET':
        footballplayer = FootballPlayer.objects.all()
        serializer = FootballPlayerSerializer(footballplayer, many=True)
        return Response(serializer.data)
