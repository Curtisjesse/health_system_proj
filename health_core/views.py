from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import AllowAny
from .models import Program, Client, Enrollment
from .serializers import (
    ProgramSerializer, ClientSerializer, ClientDetailSerializer,
    EnrollmentSerializer, ClientEnrollmentSerializer
)

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (AllowAny,)
    search_fields = ['name', 'description']

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (AllowAny,)
    search_fields = ['first_name', 'last_name', 'contact_number', 'email']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClientDetailSerializer
        return super().get_serializer_class()
    
    @extend_schema(
        request=ClientEnrollmentSerializer,
        responses={201: EnrollmentSerializer}
    )
    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        """Enroll a client in a program"""
        client = self.get_object()
        serializer = ClientEnrollmentSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                program_id = serializer.validated_data['program_id']
                program = Program.objects.get(pk=program_id)
                
                # Default values or from request
                enrollment_date = serializer.validated_data.get('enrollment_date')
                notes = serializer.validated_data.get('notes', '')
                
                # Create enrollment
                enrollment, created = Enrollment.objects.get_or_create(
                    client=client,
                    program=program,
                    defaults={
                        'enrollment_date': enrollment_date,
                        'notes': notes
                    }
                )
                
                if not created:
                    return Response(
                        {"detail": "Client already enrolled in this program"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                return Response(
                    EnrollmentSerializer(enrollment).data,
                    status=status.HTTP_201_CREATED
                )
                
            except Program.DoesNotExist:
                return Response(
                    {"detail": "Program not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = (AllowAny,)