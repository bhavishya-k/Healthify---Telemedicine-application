
from rest_framework import serializers
from .models import Patient

class PatientViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['firstname','middlename','lastname','contact','gender','dob','street','city','district','state','postalcode']

        def create(self,validated_data):
            print(validated_data)
            return Patient.objects.create(**validated_data)

        


