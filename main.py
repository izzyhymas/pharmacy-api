import json

from fastapi import FastAPI

from models import Patient


app = FastAPI()

with open("patients.json", "r") as f:
    patient_list = json.load(f)

patients: list[Patient] = []

for patient in patient_list:
    patients.append(Patient(**patient))


@app.get("/patients/")
async def list_patients() -> list[Patient]:
    return patients

@app.put("/patient/{first_name}")
async def update_patient(first_name: str, updated_patient: Patient) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients[i] = updated_patient
            return
        
@app.post("/patient")
async def add_patient(patient: Patient) -> None:
    patients.append(patient)

@app.delete("/patient/{first_name}")
async def remove_patient(first_name: str) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients.pop(i)
            return

