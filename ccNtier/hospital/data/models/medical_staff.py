# hospital/data/models/medical_staff.py
from django.db import models
from .base_model import BaseModel

class MedicalStaff(BaseModel):
    STAFF_TYPE_CHOICES = [
        ('DOCTOR', 'Médecin'),
        ('NURSE', 'Infirmier/Infirmière'),
        ('SPECIALIST', 'Spécialiste'),
        ('ADMIN', 'Personnel administratif'),
        ('TECHNICIAN', 'Technicien'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_staff_type_display()} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Membre du personnel médical"
        verbose_name_plural = "Personnel médical"
        ordering = ['staff_type', 'last_name']


from hospital.data.models.patient import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient} on {self.date}"
    

class Room(models.Model):
    number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Room {self.number} - {'Occupied' if self.is_occupied else 'Available'}"