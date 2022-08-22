from . import serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class UserRegistrationView(generics.CreateAPIView):
    
    serializer_class = serializer.UserSerializer


class DoctorTokenView(TokenObtainPairView):
   
    serializer_class = serializer.DoctorTokenSerializer


class PatientTokenView(TokenObtainPairView):

    serializer_class = serializer.PatientTokenSerializer


class HospitalTokenView(TokenObtainPairView):

    serializer_class = serializer.HospitalTokenSerializer


class PharmacyTokenView(TokenObtainPairView):

    serializer_class = serializer.PharmacyTokenSerializer


class AmbulanceTokenView(TokenObtainPairView):

    serializer_class = serializer.AmbulanceTokenSerializer


class BloodbankTokenView(TokenObtainPairView):

    serializer_class = serializer.BloodbankTokenSerializer


class LabTokenView(TokenObtainPairView):

    serializer_class = serializer.LabTokenSerializer


class UserView(generics.RetrieveAPIView):
    

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    serializer_class = serializer.UserUpdateSerializer
    permission_classes = [IsAuthenticated]


class UpdateUserView(generics.UpdateAPIView):
    

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    serializer_class = serializer.UserUpdateSerializer
    permission_classes = [IsAuthenticated]
