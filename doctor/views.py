from django.shortcuts import render
from .serializers import Doctorserializer
from user.serializer import UserSerializer
from .models import Doctor
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def DoctorView(request):
    if request.method == 'GET':
        modelobject = Doctor.objects.get(user = request.user.id)
        pythondata = Doctorserializer(modelobject)
        return Response(pythondata.data)




    





