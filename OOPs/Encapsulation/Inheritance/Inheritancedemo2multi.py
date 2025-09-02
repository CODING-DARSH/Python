class Hospital:
    def __init__(self):
        self.HospitalName="Synergy"
    def displayHospital(self):
        print(f"Name of hospital is {self.HospitalName}")
class Doctor(Hospital):
    def __init__(self):
        self.specialist="Orthopedist"
        super().__init__()
    def displayDoctor(self):
        print(f"Doctor is specialist in {self.specialist}")
class patient(Doctor):
    def __init__(self):
        self.disease="Accident"
        super().__init__()
    def displayPatient(self):
        print(f"Patient disase {self.disease}")
p=patient()
p.displayHospital()
p.displayDoctor()
p.displayPatient()