import json
import os


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

class Doctor(Person):
    def __init__(self, name, age, specialty, doctor_id):
        super().__init__(name, age)
        self.specialty = specialty
        self.doctor_id = doctor_id


patients = []
doctors = []
appointments = []
DATA_FILE = "hospital_data.json"


def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump({
            "patients": [p.__dict__ for p in patients],
            "doctors": [d.__dict__ for d in doctors],
            "appointments": appointments
        }, f)
    print("Data saved!")

def load_data():
    global patients, doctors, appointments
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            patients = [Patient(**p) for p in data.get("patients", [])]
            doctors = [Doctor(**d) for d in data.get("doctors", [])]
            appointments = data.get("appointments", [])

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    pid = input("Enter patient ID: ")
    patients.append(Patient(name, age, pid))
    print("Patient added!")

def add_doctor():
    name = input("Enter doctor name: ")
    age = int(input("Enter age: "))
    specialty = input("Enter specialty: ")
    did = input("Enter doctor ID: ")
    doctors.append(Doctor(name, age, specialty, did))
    print("Doctor added!")

def schedule_appointment():
    pid = input("Enter patient ID: ")
    did = input("Enter doctor ID: ")
    date = input("Enter appointment date (MM-DD-YYYY)): ")
    appointments.append({"patient_id": pid, "doctor_id": did, "date": date})
    print("Appointment scheduled!")

def view_records():
    print("\nPatients:")
    for p in patients:
        print(vars(p))
    print("\nDoctors:")
    for d in doctors:
        print(vars(d))
    print("\nAppointments:")
    for a in appointments:
        print(a)

def reports():
    print("\n--- Reports ---")
    print("All Patients:", [p.name for p in patients])
    print("Doctors & Specialties:", [(d.name, d.specialty) for d in doctors])
    print("Upcoming Appointments:", appointments)


def main():
    load_data()
    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. View Records")
        print("5. Generate Reports")
        print("6. Save Data")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            add_doctor()
        elif choice == "3":
            schedule_appointment()
        elif choice == "4":
            view_records()
        elif choice == "5":
            reports()
        elif choice == "6":
            save_data()
        elif choice == "7":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()


    
'''import json
import os


print("\n==== Hostpital management system ====")
print("1. Add Patient")
print("2. Add Doctor")
print("3. Schedule Appointment")
print("4. View Records")
print("5. Generate Reports")
print("6. Save")
print("7. Exit")

 

    
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

class Doctor(Person):
    def __init__(self, name, age, specialty, doctor_id):
        super().__init__(name, age)
        self.specialty = specialty
        self.doctor_id = doctor_id
        
patients = []
doctors = []
appointments = []
DATA_FILE = "hospital_data.json"

        
def save_data():
    with open("data_file.txt", "w") as f:
         print("Data saved!")

        
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    pid = input("Enter patient ID: ")
    print("patient added!")
    

def add_doctor():
    name = input("Enter doctor name: ")
    age = int(input("Enter age: "))
    specialty = input("Enter specialty: ")
    did = input("Enter doctor ID: ")
    print("Doctor added!")

def schedule_appointment():
    pid = input("Enter patient ID: ")
    did = input("Enter doctor ID: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    print("Appointment scheduled!")
    

def view_records():
    print("\nPatients:")
    

def reports():
    print("\n--- Reports ---")
    


    
choice = input("enter choice: ")

if choice == "1":
    add_patient()
elif choice == "2": 
    add_doctor()
elif choice == "3": 
    schedule_appointment()
elif choice == "4": 
    view_records()
elif choice == "5": 
    reports()
elif choice == "6": 
    save_data()
elif choice == "7":
    exit()
else:
    print("invalid choice!Try again.")'''
   








   
   
