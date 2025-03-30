# hospital/tests/test_patient_service.py
from django.test import TestCase
from hospital.business.services.patient_service import PatientService
from hospital.business.dto.patient_dto import PatientCreationDTO
from datetime import date
from hospital.business.exceptions.patient_exceptions import PatientNotFoundException

class PatientServiceTestCase(TestCase):
    def setUp(self):
        self.patient_data = PatientCreationDTO(
            first_name="Jean",
            last_name="Dupont",
            date_of_birth=date(1980, 5, 15),
            gender="M",
            address="123 Rue de Paris",
            phone_number="0123456789",
            email="jean.dupont@example.com"
        )

    def test_create_and_get_patient(self):
        # Test creation
        patient_dto = PatientService.create_patient(self.patient_data)
        self.assertIsNotNone(patient_dto.id)
        self.assertEqual(patient_dto.first_name, "Jean")
        
        # Test retrieval
        retrieved_patient = PatientService.get_patient_by_id(patient_dto.id)
        self.assertEqual(retrieved_patient.first_name, "Jean")
        
    def test_get_nonexistent_patient(self):
        with self.assertRaises(PatientNotFoundException):
            PatientService.get_patient_by_id(999)