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
        """This is what nightmares look like"""
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
        self.letter_grade = None
        # Yeah idk if this is okay, but it works
        self.run()

    def run(self):
        self.student_name = self.get_student_name()
        # get assignment grades and calc overall grade
        self.assignment_grades = self.get_grades("Assignment", self.assignemt_count)
        self.assignment_overall_grade = self.get_weighted_grade(self.assignment_grades, .2)
        # get quiz grades and calc overall grade
        self.quiz_grades = self.get_grades("Quiz", self.quiz_count)
        self.quiz_overall_grade = self.get_weighted_grade(self.quiz_grades, .2)
        # get project grades and calc overall grade
        self.project_grades = self.get_grades("Project", self.project_count)
        self.project_overall_grade = self.get_weighted_grade(self.project_grades, .5)
        # get absent count and calc grade
        self.absent_count = self.get_absent_amount()
        self.absent_grade = self.get_absent_grade(self.absent_count)
        # creates total grade 
        self.total_grade = self.get_total_grade(self.assignment_overall_grade,
                                                self.quiz_overall_grade,
                                                self.project_overall_grade,
                                                self.absent_grade)
        # creates letter grade
        self.letter_grade = self.get_letter_grade(self.total_grade)

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
        """gets grade per type"""
        # Need to add protection for max integer amount
        # also, these should be floats. Yikes
        grades = []
        for i in range(1, count+1):
            prompt = f"Enter grade for {type} #{i}: "
            while len(grades) < i:
                # CHANGE TO FLOATS
                cmd = IntegerForm.check_integer(self, input(prompt))
                if not cmd:
                    print("Please enter a float!")
                else:
                    grades.append(cmd)
        return grades

    def get_absent_amount(self):
        """gets absent amount"""
        prompt = f"How many class sessions did {self.student_name} miss this semester? "
        while not self.absent_count:
            cmd = IntegerForm.check_integer(self, input(prompt))
            if not cmd:
                print("Please enter an integer!")
            else:
                return cmd
    
    def get_absent_grade(self, amount):
        """creates the participation grade"""
        # Should probably change all these 'gets' to 'sets'
        if amount > 3 and amount < 9:
            return (10 - 2 * (amount - 3))
        elif amount <= 3:
            return 10
        else:
            return 0

    def get_weighted_grade(self, arr, weight):
        """calculates the weighted grade per grade type of a student"""
        avg_grade = sum(arr) / len(arr)
        return avg_grade * weight
    
    def get_total_grade(self, assignment, quiz, project, absent):
        """adds all the grade types together"""
        # pre weighted
        total = assignment + quiz + project + absent
        return round(total, 2)
    
    def get_letter_grade(self, total_grade):
        """creates letter grade"""
        # VERIFY AGAINST RUBRIC
        if total_grade >= 92:
            return 'A'
        elif total_grade >= 86:
            return 'B'
        elif total_grade >= 76:
            return 'C'
        elif total_grade >= 64:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        """for the view feature primarily"""
        # This is mostly for the view feature
        # Maybe spice this up a bit
        return f'{self.student_name} -- {self.total_grade}%'

