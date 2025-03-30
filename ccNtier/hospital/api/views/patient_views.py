# hospital/api/views/patient_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from hospital.business.services.patient_service import PatientService
from hospital.business.dto.patient_dto import PatientCreationDTO, PatientUpdateDTO
from hospital.business.exceptions.patient_exceptions import PatientNotFoundException

class PatientListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = PatientService.get_all_patients()
        return Response([patient.__dict__ for patient in patients])

    def post(self, request):
        try:
            creation_dto = PatientCreationDTO(**request.data)
            patient = PatientService.create_patient(creation_dto)
            return Response(patient.__dict__, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PatientDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            patient = PatientService.get_patient_by_id(pk)
            return Response(patient.__dict__)
        except PatientNotFoundException as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            update_dto = PatientUpdateDTO(**request.data)
            patient = PatientService.update_patient(pk, update_dto)
            return Response(patient.__dict__)
        except PatientNotFoundException as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            PatientService.delete_patient(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PatientNotFoundException as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

class PatientSearchView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        search_term = request.query_params.get('q', '')
        patients = PatientService.search_patients(search_term)
        return Response([patient.__dict__ for patient in patients])