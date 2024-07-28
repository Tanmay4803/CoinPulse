from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Alert
from .serializers import AlertSerializer

@api_view(['GET'])
def getalerts(request):
    users = Alert.objects.all()
    serializer = AlertSerializer(users, many=True)
    return Response({
        "message": "Retrieved all alerts",
        "data": serializer.data
    })

@api_view(['GET'])
def getalert(request, pk):
    user = Alert.objects.get(id=pk)
    serializer = AlertSerializer(user, many=False)
    return Response({
        "message": f"Retrieved alert with id {pk}",
        "data": serializer.data
    })

@api_view(['POST'])
def addalert(request):
    serializer = AlertSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Added new alert",
            "data": serializer.data
        })
    return Response({
        "message": "Failed to add alert",
        "errors": serializer.errors
    })

@api_view(['PUT'])
def updatealert(request, pk):
    user = Alert.objects.get(id=pk)
    serializer = AlertSerializer(instance = user, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": f"Updated alert with id {pk}",
            "data": serializer.data
        })
    return Response({
        "message": f"Failed to update alert with id {pk}",
        "errors": serializer.errors
    })

@api_view(['DELETE'])
def deletealert(request, pk):
    user = Alert.objects.get(id=pk)
    user.delete()
    return Response({
        "message": f"Deleted alert with id {pk}"
    })
