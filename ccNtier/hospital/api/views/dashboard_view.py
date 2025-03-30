from rest_framework.views import APIView
from rest_framework.response import Response
from hospital.data.models.patient import Patient
from hospital.data.models.room import Room

class DashboardView(APIView):
    def get(self, request):
        total_patients = Patient.objects.count()
        occupied_rooms = Room.objects.filter(is_occupied=True).count()
        return Response({
            "total_patients": total_patients,
            "occupied_rooms": occupied_rooms,
        })