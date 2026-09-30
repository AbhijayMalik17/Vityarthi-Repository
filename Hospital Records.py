from pathlib import Path


FILENAME = Path.home() / "Desktop" / "patients.txt"

patients = {}

def load_data():
    """Reads records from patients.txt on Desktop if it exists."""
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    p_id, name, age, diagnosis = line.split(",")
                    patients[p_id] = {
                        "Name": name,
                        "Age": age,
                        "Diagnosis": diagnosis
                    }
    except FileNotFoundError:
        
        pass

def save_data():
    """Saves/updates patients.txt directly on your Desktop."""
    with open(FILENAME, "w") as file:
        for p_id, info in patients.items():
            file.write(f"{p_id},{info['Name']},{info['Age']},{info['Diagnosis']}\n")

def display_menu():
    print("\n--- Hospital Record Manager ---")
    print("1. Add a new patient")
    print("2. View patient details")
    print("3. List all patients")
    print("4. Discharge/Remove a patient")
    print("5. Exit")

def add_patient():
    patient_id = input("Enter Patient ID (e.g., 101): ")
    if patient_id in patients:
        print("Error: Patient ID already exists!")
        return

    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Diagnosis/Disease: ")

    patients[patient_id] = {
        "Name": name,
        "Age": age,
        "Diagnosis": disease
    }
    save_data()
    print(f"\nSuccess: Patient {name} saved to {FILENAME}!")

def view_patient():
    patient_id = input("Enter Patient ID to search: ")
    if patient_id in patients:
        print("\n--- Patient Details ---")
        for key, value in patients[patient_id].items():
            print(f"{key}: {value}")
    else:
        print("Error: Patient not found.")

def list_patients():
    if not patients:
        print("No patients currently in the system.")
        return

    print("\n--- All Patients ---")
    for p_id, info in patients.items():
        print(f"ID: {p_id} | Name: {info['Name']} | Diagnosis: {info['Diagnosis']}")

def discharge_patient():
    patient_id = input("Enter Patient ID to discharge: ")
    if patient_id in patients:
        removed_patient = patients.pop(patient_id)
        save_data()
        print(f"\nSuccess: Patient {removed_patient['Name']} discharged and file updated on Desktop.")
    else:
        print("Error: Patient not found.")


print(f"Saving data to: {FILENAME}")
load_data()

while True:
    display_menu()
    choice = input("\nEnter choice (1-5): ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        view_patient()
    elif choice == '3':
        list_patients()
    elif choice == '4':
        discharge_patient()
    elif choice == '5':
        print("Exiting system. All changes saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-5.")