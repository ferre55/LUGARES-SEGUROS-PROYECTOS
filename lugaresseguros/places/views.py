from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from places.models import Place   #import model
from places.serializers import PlaceSerializer # import serializers


#First View

class PlaceView(APIView):
    def get(self,request):
        #Query --> Petición base de datos
        #QuerySet --> Resultado de una Query. Lista de Objetos.

        places  = Place.objects.all ()
        print(places)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PlaceSingleView(APIView):
    def put(self,request,id):
        place = Place.objects.get(id=id)
        serializer= PlaceSerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        place= Place.objects.get(id=id)
        place.delete()
        return Response({"message": "Eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
