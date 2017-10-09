from rest_framework import serializers
from footballplayer.models import FootballPlayer

class FootballPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballPlayer
        fields = ('name', 'team', 'nationality', 'age', 'shirt_number', 'position')
