"""
Create class for each student that conatins the logic for
their grades, days missing, and names
"""
from forms.name_form import NameForm
from forms.integer_form import IntegerForm

class Student:
    def __init__(self, a_count, q_count, p_count):
        self.student_name = None
        self.assignemt_count = a_count
        self.assignment_grades = []
        self.assignment_overall_grade = None
        self.quiz_count = q_count
        self.quiz_grades = []
        self.quiz_overall_grade = None
        self.project_count = p_count
        self.project_grades = []
        self.project_overall_grade = None
        self.absent_count = None
        self.absent_grade = None
        self.run()

    def run(self):
        self.student_name = self.get_student_name()
        self.get_assignment_grades = self.get_assignment_grades(self.assignemt_count)
        self.get_quiz_grades = self.get_quiz_grades(self.quiz_count)
        self.get_project_grades = self.get_project_grades(self.project_count)

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
                self.student_name = cmd
    
    def get_assignment_grades(self, count):
        for i in range(0, count+1):
            prompt = f"Enter grade for Assignment #{i}: "
            while len(self.assignment_grades) < i:
                cmd = IntegerForm.check_integer(self, input(prompt))
                if not cmd:
                    print("Please enter a float!")
                else:
                    self.assignment_grades.append(cmd)

    def get_quiz_grades(self, count):
        for i in range(0, count+1):
            prompt = f"Enter grade for Quiz #{i}: "
            while len(self.assignment_grades) < i:
                cmd = IntegerForm.check_integer(self, input(prompt))
                if not cmd:
                    print("Please enter a float!")
                else:
                    self.quiz_grades.append(cmd)

    def get_project_grades(self, count):
        for i in range(0, count+1):
            prompt = f"Enter grade for Project #{i}: "
            while len(self.assignment_grades) < i:
                cmd = IntegerForm.check_integer(self, input(prompt))
                if not cmd:
                    print("Please enter a float!")
                else:
                    self.project_grades.append(cmd)

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
