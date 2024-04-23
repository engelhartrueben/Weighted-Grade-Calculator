"""
Create class for each student that conatins the logic for
their grades, days missing, and names
"""
from forms.name_form import NameForm
from forms.integer_form import IntegerForm

class Student:
    def __init__(self, 
                 a_count, 
                 q_count, 
                 p_count, 
                 student_name=None):
        self.student_name = student_name
        self.assignemt_count = a_count
        self.assignment_grades = None
        self.assignment_overall_grade = None
        self.quiz_count = q_count
        self.quiz_grades = None
        self.quiz_overall_grade = None
        self.project_count = p_count
        self.project_grades = None
        self.project_overall_grade = None
        self.absent_count = None
        self.absent_grade = None
        self.total_grade = None
        self.run()

    def run(self):
        self.student_name = self.get_student_name()
        self.assignment_grades = self.get_grades("Assignment", self.assignemt_count)
        self.quiz_grades = self.get_grades("Quiz", self.quiz_count)
        self.project_grades = self.get_grades("Project", self.project_count)
        print(self.student_name, self.total_grade)
        return [
            self.student_name,
            self.total_grade
        ]

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
                return cmd
            
    def get_grades(self, type, count):
        grades = []
        for i in range(1, count+1):
            prompt = f"Enter grade for {type} #{i}: "
            while len(grades) < i:
                cmd = IntegerForm.check_integer(self, input(prompt))
                if not cmd:
                    print("Please enter a float!")
                else:
                    grades.append(cmd)
        return grades

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

    def get_weighted_grade(self, arr, weight):
        avg_grade = sum(arr) / len(arr)
        return avg_grade * weight
    
    def get_total_grade(self):
        self.total_grade = (
            self.assignment_overall_grade +
            self.quiz_overall_grade +
            self.assignment_overall_grade
        )
