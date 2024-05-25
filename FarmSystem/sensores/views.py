from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SensorData
from .serializers import SensorDataSerializer

@api_view(['POST'])
def sensor_data(request):
    if request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
