# hospital/business/services/patient_service.py
from ..dto.patient_dto import PatientDTO, PatientCreationDTO, PatientUpdateDTO
from ..exceptions.patient_exceptions import PatientNotFoundException
from hospital.data.repositories.patient_repository import PatientRepository

class PatientService:
    @staticmethod
    def get_all_patients():
        patients = PatientRepository.get_all_patients()
        return [PatientDTO.from_entity(patient) for patient in patients]

    @staticmethod
    def get_patient_by_id(patient_id):
        patient = PatientRepository.get_patient_by_id(patient_id)
        if not patient:
            raise PatientNotFoundException(patient_id)
        return PatientDTO.from_entity(patient)

    @staticmethod
    def create_patient(patient_creation_dto: PatientCreationDTO):
        patient_data = patient_creation_dto.to_dict()
        patient = PatientRepository.create_patient(patient_data)
        return PatientDTO.from_entity(patient)

    @staticmethod
    def update_patient(patient_id, patient_update_dto: PatientUpdateDTO):
        patient = PatientRepository.get_patient_by_id(patient_id)
        if not patient:
            raise PatientNotFoundException(patient_id)
        
        update_data = patient_update_dto.to_dict()
        updated_patient = PatientRepository.update_patient(patient_id, update_data)
        return PatientDTO.from_entity(updated_patient)

    @staticmethod
    def delete_patient(patient_id):
        if not PatientRepository.get_patient_by_id(patient_id):
            raise PatientNotFoundException(patient_id)
        return PatientRepository.delete_patient(patient_id)

    @staticmethod
    def search_patients(search_term):
        patients = PatientRepository.search_patients(search_term)
        return [PatientDTO.from_entity(patient) for patient in patients]