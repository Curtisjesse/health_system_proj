from rest_framework import serializers
from .models import Program, Client, Enrollment

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    program_name = serializers.ReadOnlyField(source='program.name')
    
    class Meta:
        model = Enrollment
        fields = ['id', 'program', 'program_name', 'enrollment_date', 'notes', 'status']

class ClientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'age', 
                 'gender', 'contact_number', 'email', 'address', 'created_at']
    
    def get_age(self, obj):
        return obj.get_age()

class ClientDetailSerializer(ClientSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    
    class Meta(ClientSerializer.Meta):
        fields = ClientSerializer.Meta.fields + ['enrollments']

class ClientEnrollmentSerializer(serializers.Serializer):
    program_id = serializers.IntegerField()
    enrollment_date = serializers.DateField(required=False)
    notes = serializers.CharField(required=False, allow_blank=True)