# hospital/business/exceptions/patient_exceptions.py
class PatientNotFoundException(Exception):
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.message = f"Patient avec l'ID {patient_id} non trouvé"
        super().__init__(self.message)