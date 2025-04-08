''''
1. make a new Python class
2. input patient name, age, date of latest admission and medical history
3. print all these details in a single line
'''
class patient (object):
    def __init__(self, name, age, date, medical_history):
        self.name = name
        self.age = age
        self.date = date
        self.medical_history = medical_history
    
    def print(self):
        print(f"Name: {self.name}, Age: {self.age}, Last Admission Date: {self.date}, Medical History: {self.medical_history}")

patient1 = patient(name="Zhang San", age=18, date="2025-2-30", medical_history="fever, stomachache")
