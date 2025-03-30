# hospital/business/dto/patient_dto.py
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class PatientDTO:
    id: int
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    address: str
    phone_number: str
    email: Optional[str]
    blood_type: Optional[str]
    allergies: Optional[str]
    insurance_number: Optional[str]
    emergency_contact: Optional[str]
    emergency_phone: Optional[str]

    @classmethod
    def from_entity(cls, patient):
        return cls(
            id=patient.id,
            first_name=patient.first_name,
            last_name=patient.last_name,
            date_of_birth=patient.date_of_birth,
            gender=patient.gender,
            address=patient.address,
            phone_number=patient.phone_number,
            email=patient.email,
            blood_type=patient.blood_type,
            allergies=patient.allergies,
            insurance_number=patient.insurance_number,
            emergency_contact=patient.emergency_contact,
            emergency_phone=patient.emergency_phone
        )

@dataclass
class PatientCreationDTO:
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    address: str
    phone_number: str
    email: Optional[str] = None
    blood_type: Optional[str] = None
    allergies: Optional[str] = None
    insurance_number: Optional[str] = None
    emergency_contact: Optional[str] = None
    emergency_phone: Optional[str] = None

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender,
            'address': self.address,
            'phone_number': self.phone_number,
            'email': self.email,
            'blood_type': self.blood_type,
            'allergies': self.allergies,
            'insurance_number': self.insurance_number,
            'emergency_contact': self.emergency_contact,
            'emergency_phone': self.emergency_phone
        }

@dataclass
class PatientUpdateDTO:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    blood_type: Optional[str] = None
    allergies: Optional[str] = None
    insurance_number: Optional[str] = None
    emergency_contact: Optional[str] = None
    emergency_phone: Optional[str] = None

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}