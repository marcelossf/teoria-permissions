from rest_framework.views import APIView
from rest_framework.response import Response
from musicians.models import Musician
from musicians.serializers import MusicianSerializer

class MusicianView(APIView):
    
    def get(self, request):
        musicians = Musician.objects.all()

        serializer = MusicianSerializer(musicians, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = MusicianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        musician = Musician.objects.create(**serializer.validated_data)
        serializer = MusicianSerializer(musician)
        
        return Response(serializer.data)
