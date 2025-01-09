import requests

FHIR_BASE_URL = "http://localhost:8080/fhir/"

def get_patient_records(patient_id):
    url = f"{FHIR_BASE_URL}/Patient/{patient_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
