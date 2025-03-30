# hospital/data/repositories/patient_repository.py
from django.core.exceptions import ObjectDoesNotExist
from ..models.patient import Patient

class PatientRepository:
    @staticmethod
    def get_all_patients():
        return Patient.objects.all()

    @staticmethod
    def get_patient_by_id(patient_id):
        try:
            return Patient.objects.get(id=patient_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def create_patient(patient_data):
        return Patient.objects.create(**patient_data)

    @staticmethod
    def update_patient(patient_id, patient_data):
        patient = PatientRepository.get_patient_by_id(patient_id)
        if patient:
            for key, value in patient_data.items():
                setattr(patient, key, value)
            patient.save()
            return patient
        return None

    @staticmethod
    def delete_patient(patient_id):
        patient = PatientRepository.get_patient_by_id(patient_id)
        if patient:
            patient.delete()
            return True
        return False

    @staticmethod
    def search_patients(search_term):
        return Patient.objects.filter(
            models.Q(first_name__icontains=search_term) |
            models.Q(last_name__icontains=search_term) |
            models.Q(insurance_number__icontains=search_term)
        )