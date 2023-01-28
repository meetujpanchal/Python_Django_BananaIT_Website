from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from banana_web_api.models import person
from .serializers import PersonSerializers
from bananait_api import serializers

@api_view(['GET'])
def apiOverview(request):
    bananait_api_urls = {
        'Data-List':'/data/',
        'Detailed-Data':'detail-data',
        'Add-Data':'/add/',
        'Update-Data':'/update/',
        'Delete-Data':'/delete/',
    }

    return Response(bananait_api_urls)

@api_view(['GET'])
def detailview(request,pk):
    persons = person.objects.get(id=pk)
    serializer = PersonSerializers(persons, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getData(request):
    persons = person.objects.all()
    serializer = PersonSerializers(persons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPerson(request):
    serializer = PersonSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatePerson(request, pk):
    pers = person.objects.get(id=pk)
    serializer = PersonSerializers(instance=pers ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)        

@api_view(['DELETE'])
def deleteperson(request, pk):
    persons = person.objects.get(id=pk)
    persons.delete()
    return Response('Person Deleted Successfully!!')    