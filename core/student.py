"""
Create class for each student that conatins the logic for
their grades, days missing, and names
"""
from forms.name_form import NameForm
from forms.integer_form import IntegerForm
from core.engine import AppEngine

class Student(AppEngine):
    def __init__(self):
        self.student_name = None
        self.assignment_grades = None
        self.assignment_overall_grade = None
        self.quiz_grades = None
        self.quiz_overall_grade = None
        self.project_grades = None
        self.project_overall_grade = None
        self.absent_count = None
        self.absent_grade = None

    def run(self):
        self.student_name = self.get_student_name(self)
        self.get_assignment_grades = self.get_assignment_grades(self, self.assignment_count)
        self.get_quiz_grades = self.get_quiz_grades(self, self.quiz_count)
        self.get_project_grades = self.get_project_grades(self, self.project_count)

    def get_student_name(self):
        """sets students name"""
        # will have to make this dynamic
        # in order to support more than one
        # studen. i.e. an entire class
        prompt = "Enter Student's Name: "
        while not self.student_name:
            cmd = NameForm.check_name(self, input(prompt))
            if not cmd:
                # not sending to self.message
                # containing to this func
                print("Invalid Student Name!")
            else:
                self.name = cmd
    
    def get_assignment_grades(self, count):
        pass

    def get_quiz_grades(self, count):
        pass

    def get_project_grades(self, count):
        pass

    def get_absent_amount(self):
        prompt = f"How many class sessions did {self.student_name} miss this semester? "
        while not self.absent_count:
            cmd = IntegerForm.check_integer(self, input(prompt))
            if not cmd:
                print("Please enter an integer!")
            else:
                self.absent_count = cmd
        if self.absent_count > 3:
            self.absent_grade = (.1 - .02 * (self.absent_count - 3))
        else:
            self.absent_grade = .1
