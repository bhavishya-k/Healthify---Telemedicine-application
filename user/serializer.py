from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import user as USER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ['email','password','role']
    

    

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.pop('role', None)
        print(validated_data)

        if role == USER.ADMIN: 
            print('Reached here')
            raise serializers.ValidationError('You cannot create admin user')
        
        
        
        if role == USER.DOCTOR: 
            
            user = USER.objects.create_doctor(**validated_data)
            user.set_password(password)
            user.save()
            return user

        if role == USER.PATIENT:
            user = USER.objects.create_patient(**validated_data)
            user.set_password(password)
            user.save()
            return user

        if role == USER.HOSPITAL:
            user = USER.objects.create_hospital(**validated_data)
            user.set_password(password)
            user.save()
            return user

        if role == USER.PHARMACY:
            user = USER.objects.create_pharmacy(**validated_data)
            user.set_password(password)
            user.save()
            return user

        if role == USER.AMBULANCE:
            user = USER.objects.create_ambulance(**validated_data)
            user.set_password(password)
            user.save()
            return user

        if role == USER.BLOODBANK:
            user = USER.objects.create_bloodbank(**validated_data)
            user.set_password(password)
            user.save()
            return user

        if role == USER.LAB:
            user = USER.objects.create_lab(**validated_data)
            user.set_password(password)
            user.save()
            return user


class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)
    old_password = serializers.CharField(write_only=True, required=False)
    new_password = serializers.CharField(min_length=5, write_only=True, required=False)

    def validate(self, attrs):
        user = self.context['request'].user
        old_password = attrs.get('old_password', None)
        new_password = attrs.get('new_password', None)
        if old_password != None and new_password == None:
            raise serializers.ValidationError({"detail": "You need to enter the new password!"})
        if old_password == None and new_password != None:
            raise serializers.ValidationError({"detail": "You need to enter the old password!"})
        if old_password != None and not user.check_password(old_password):
            raise serializers.ValidationError({"detail": "Your old password  was entered incorrectly. Please enter it again!"})
        
        
        return attrs

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('new_password', instance.password)
        instance.set_password(password)
        instance.save()
        return instance


class DoctorTokenSerializer(TokenObtainPairSerializer):
    ''' Token Doctor Serializer '''
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.DOCTOR:
        raise serializers.ValidationError({"detail": "You are not a doctor"})
       return token


class PatientTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.PATIENT:
        raise serializers.ValidationError({"detail": "You are not a patient"})
       return token


class HospitalTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.HOSPITAL:
        raise serializers.ValidationError({"detail": "You are not a hospital"})
       return token


class PharmacyTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.PHARMACY:
        raise serializers.ValidationError({"detail": "You are not a pharmacy"})
       return token


class AmbulanceTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.AMBULANCE:
        raise serializers.ValidationError({"detail": "You are not an ambulance"})
       return token


class BloodbankTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.BLOODBANK:
        raise serializers.ValidationError({"detail": "You are not a bloodbank"})
       return token


class LabTokenSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
       token = super().get_token(user)
       if user.role != USER.LAB:
        raise serializers.ValidationError({"detail": "You are not a lab"})
       return token

        

        
