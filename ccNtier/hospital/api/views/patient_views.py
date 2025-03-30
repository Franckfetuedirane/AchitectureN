from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hospital.business.services.patient_service import create_patient, get_patient, update_patient, delete_patient 

class PatientView(APIView):
    def post(self, request):
        patient = create_patient(request.data)
        return Response({"id": patient.id}, status=status.HTTP_201_CREATED)

    def get(self, request, patient_id):
        patient = get_patient(patient_id)
        return Response({"id": patient.id, "name": f"{patient.first_name} {patient.last_name}"})

    def put(self, request, patient_id):
        patient = update_patient(patient_id, request.data)
        return Response({"id": patient.id, "updated": True})

    def delete(self, request, patient_id):
        delete_patient(patient_id)
        return Response({"deleted": True}, status=status.HTTP_204_NO_CONTENT)
    
    