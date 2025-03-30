from hospital.data.models.patient import Patient

def create_patient(data):
    return Patient.objects.create(**data)

def get_patient(patient_id):
    return Patient.objects.get(id=patient_id)

def update_patient(patient_id, data):
    patient = Patient.objects.get(id=patient_id)
    for key, value in data.items():
        setattr(patient, key, value)
    patient.save()
    return patient

def delete_patient(patient_id):
    Patient.objects.get(id=patient_id).delete()