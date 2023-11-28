import tkinter as tk
from tkinter import messagebox #UI
import sounddevice as sd #Sound simulation (can be ignored)
import numpy as np

class AudioRecordingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Details")
        self.root.configure(bg='#FFFFE0')  # For Setting yellow background colour

        # Variables to store patient details
        self.name_var = tk.StringVar() #name
        self.gender_var = tk.StringVar() #Gender
        self.age_var = tk.StringVar() #Age
        self.phone_var = tk.StringVar() #Phone
        self.aadhar_var = tk.StringVar() #Aadhar

        #  initial screen for patient  details
        self.create_input_screen()

    def create_input_screen(self):
        input_frame = tk.Frame(self.root, bg='#FFFFE0')  
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Patient Details", font=("Helvetica", 16, "bold"), pady=10).grid(row=0, columnspan=2) #Title

        tk.Label(input_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5) #Text label
        tk.Entry(input_frame, textvariable=self.name_var).grid(row=1, column=1, padx=10, pady=5) #Text entry field

        tk.Label(input_frame, text="Gender:").grid(row=2, column=0, padx=10, pady=5)
        gender_options = ["Male", "Female", "Others"] #Radio buttons for gender
        self.gender_var.set(gender_options[0])  # Set default value
        tk.OptionMenu(input_frame, self.gender_var, *gender_options).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Age:").grid(row=3, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.age_var, validate="key", validatecommand=(self.validate_age, '%P')).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Phone:").grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.phone_var, validate="key", validatecommand=(self.validate_phone, '%P')).grid(row=4, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Aadhar:").grid(row=5, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.aadhar_var, validate="key", validatecommand=(self.validate_aadhar, '%P')).grid(row=5, column=1, padx=10, pady=5)

        tk.Button(input_frame, text="Next", command=self.create_instruction_screen).grid(row=6, columnspan=2, pady=10)

    def create_instruction_screen(self): #Input Validation
        if not self.validate_age(self.age_var.get()): #Age must be between 0 and 150
            messagebox.showwarning("Invalid Age", "Please enter a valid age (between 1 and 150).")
            return

        if not self.validate_phone(self.phone_var.get()): #Phone number must be a 10 digit number
            messagebox.showwarning("Invalid Phone Number", "Please enter a valid phone number with 10 digits.")
            return

        if not self.validate_aadhar(self.aadhar_var.get()): #Aadhar must be 12 digits
            messagebox.showwarning("Invalid Aadhar Number", "Please enter a valid Aadhar number with 12 digits.")
            return

        self.root.withdraw()  # Hide the input screen
        instruction_root = tk.Tk()
        instruction_root.title("Audio Recording Instructions") #Audio recording screen
        instruction_root.configure(bg='#FFFFE0')  

        instruction_label = tk.Label(instruction_root, text="Click 'Start Recording' and 'OK' to start recording your voice for 10s.\nRecording will be automatically completed.")
        instruction_label.pack(pady=10) #Audio recording instructions

        tk.Button(instruction_root, text="Start Recording", command=self.record_audio).pack(pady=10) #Audio recording simulation button

        tk.Button(instruction_root, text="Complete", command=self.show_thank_you_screen).pack(pady=10) # Complete and close everything button

    def record_audio(self):
        # Simulate recording audio for 10 seconds
        messagebox.showinfo("Recording", "Recording audio for 10 seconds...")

        fs = 44100  
        duration = 10  # Recording duration in seconds
        recording = sd.rec(int(fs * duration), channels=2, dtype=np.int16)
        sd.wait()

        messagebox.showinfo("Recording", "Recording complete!")

    def show_thank_you_screen(self):
        # Thank you message
        messagebox.showinfo("Thank You", "Thank you for using the Audio Recording App!")
        exit()

    def validate_numbers(self, value): #Digit validation for Phone, Age and Aadhaar
        return value.isdigit()

    def validate_age(self, value):
        if value.isdigit():
            age = int(value)
            return 1 <= age <= 150
        return False

    def validate_phone(self, value):
        return value.isdigit() and len(value) == 10

    def validate_aadhar(self, value):
        return value.isdigit() and len(value) == 12


if __name__ == "__main__": #Call main function to run the program and render the tkinter
    root = tk.Tk()
    app = AudioRecordingApp(root)
    root.mainloop()
