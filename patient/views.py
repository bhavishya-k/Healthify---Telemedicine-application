from rest_framework import serializers
from .serializers import PatientViewSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def PatientView(request):
    if request.method == 'GET':
        if request.user.role != 'PATIENT':
            raise serializers.ValidationError('You are not a patient')
        modelobject = Patient.objects.get(user = request.user.id)
        pythondata = PatientViewSerializer(modelobject)
        return Response(pythondata.data)

    if request.method == 'POST':
        print(request.data)
        if request.user.role != 'PATIENT':
            raise serializers.ValidationError('You are not a patient')
        
        modelobject = PatientViewSerializer(data=request.data)
        if modelobject.is_valid():
            
            modelobject.save(user = request.user)
            return Response({'Response':'Data Created'})
        return Response(serializers.Serializer.errors)

    if request.method == 'PUT':
        if request.user.role != 'PATIENT':
            raise serializers.ValidationError('You are not a patient')
        modelobject = Patient.objects.get(user = request.user.id)
        obj = PatientViewSerializer(modelobject,data=request.data, partial = True)
        if obj.is_valid():
            obj.save()
            return Response({'Response':'Object Updated'})
        return Response(serializers.Serializer.errors)

    if request.method == 'DELETE':
        if request.user.role != 'PATIENT':
            raise serializers.ValidationError('You are not a patient')
        modelobject = Patient.objects.get(user = request.user.id)
        modelobject.delete()
        return Response({'response':'Data Deleted'})

        





