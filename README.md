Simple Hospital Patient Record Manager

A lightweight, beginner-friendly Command Line Interface (CLI) application built with pure Python. It allows users to register, inspect, list, and discharge patient records while automatically persisting and syncing all data to a text file saved directly to your computer's Desktop.

Project Description

The Hospital Patient Record Manager demonstrates practical, fundamentals-focused Python programming without requiring external libraries or complex database software.

Instead of keeping records in temporary program memory or buried inside project subfolders, this program uses Python's built-in pathlib module to detect the operating system's active user environment and store records directly on the Desktop (patients.txt). Any addition or discharge is instantly synced to disk, ensuring no data loss when the application exits.

Key Features

Direct Desktop Sync: Saves and updates patients.txt directly on your Desktop for easy access.

Cross-Platform Compatibility: Uses dynamic path resolution (Path.home()) to work seamlessly across Windows, macOS, and Linux without manual path edits.

Patient Registration: Add patients with an ID, Name, Age, and Diagnosis.

Instant Record Search: Look up specific patient details by Patient ID.

Roster Overview: Display a clean summary list of all admitted patients.

Discharge Management: Remove discharged patients from active records and immediately update the desktop file.

Zero Dependencies: Requires only standard Python 3 (no pip install needed).

Storage & File Structure

Records are saved to a file named patients.txt located on your Desktop:

File Location:

Windows: C:\Users\<YourUsername>\Desktop\patients.txt

macOS: /Users/<YourUsername>/Desktop/patients.txt

Linux: /home/<YourUsername>/Desktop/patients.txt

Storage Format: Comma-Separated Values (CSV-style per line):

<Patient_ID>,<Name>,<Age>,<Diagnosis>


Example patients.txt Content:

101,John Doe,34,Hypertension
102,Jane Smith,28,Acute Bronchitis


Getting Started

Prerequisites

Python 3.6 or higher installed on your computer.

Running the Program

Save the code into a Python script named hospital_manager.py.

Open your terminal or Command Prompt and run:

python hospital_manager.py


Upon launch, the console prints the exact path where patients.txt is located on your Desktop.

Application Menu

When the program runs, you will interact with the following CLI menu:

Saving data to: C:\Users\<Username>\Desktop\patients.txt

--- Hospital Record Manager ---
1. Add a new patient
2. View patient details
3. List all patients
4. Discharge/Remove a patient
5. Exit


1: Prompts for patient information and appends/saves to Desktop.

2: Queries an existing patient by their unique ID.

3: Displays all active patient records.

4: Discharges a patient, removes them from memory, and refreshes the desktop file.

5: Safely closes the program.

Built With

Python 3

pathlib for dynamic cross-platform desktop path handling

Built-in file I/O (open(), read(), write())

Native dictionaries for in-memory records
