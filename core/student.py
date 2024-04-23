"""
Create class for each student that conatins the logic for
their grades, days missing, and names
"""
from forms.name_form import NameForm

class Student:
    def __init__(self):
        self.student_name = None
        self.absent_count = None

    def run(self):
        self.student_name = self.get_student_name()

    def get_student_name(self):
        """sets students name"""
        # will have to make this dynamic
        # in order to support more than one
        # studen. i.e. an entire class
        prompt = "Enter Student's Name: "
        while not self.student_name:
            cmd = input(prompt)
            name = NameForm.check_name(cmd)
            if not name:
                # not sending to self.message
                # containing to this func
                print("Invalid Student Name!")
            else:
                self.name = name