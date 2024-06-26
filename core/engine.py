from forms.string_form import StringForm
from forms.integer_form import IntegerForm
from core.student import Student

class AppEngine:
    def __init__(self, grade_item=None):
        self.message = None
        self.continue_execution = True
        self.grade_item = grade_item
        self.class_name = None
        self.assignment_count = None
        self.quiz_count = None
        self.project_count = None
        self.class_grades = {}
        self.student_id = 0
    
    def get_class_name(self):
        """sets class name for this session"""
        prompt = "Enter Class Name: "
        # If this funciton is ever recalled
        # Like when wanting to change the class name
        # resets back to None
        self.class_name = None
        while not self.class_name:
            class_name = StringForm.check_string(self, input(prompt))
            if not class_name:
                # Not entirely neccessary due to how
                # check_string works. Not many things to 
                # throw it off. Oh well. At least it formats
                print("Invalid Class Name!")
            else:
                self.class_name = class_name
    
    def get_counts(self, type=None):
        """gets total amount of counts of"""
        if type:
            counts = [type]
        else:
            counts = [
                "Assignments",
                "Quizzes",
                "Projects"
            ]
        for part in counts:
            prompt = f"Enter the number of {part}: "
            while True:
                cmd = IntegerForm.check_integer(self, input(prompt))
                if not cmd:
                    print("Please enter an integer!")
                else:
                    break
            if part == "Assignments":
                self.assignment_count = cmd
            elif part == "Quizzes":
                self.quiz_count = cmd
            else:
                self.project_count = cmd
        if len(counts) > 1:
            prompt = (f"You have entered:"
                      f"\nAssignments: {self.assignment_count}"
                      f"\nQuizzes:     {self.quiz_count}"
                      f"\nProjects:    {self.project_count}")
            prompt = prompt + "\nIs this correct? (y/n) "
            cmd = input(prompt)
            if cmd in ('n'):
                self.get_counts()
    
    def get_student_information(self):
        student_dict = self.class_grades
        student_dict.update({self.student_id : Student(self.assignment_count,
                                                              self.quiz_count,
                                                              self.project_count)})
        self.class_grades = student_dict
        self.student_id+=1
    
    def preview_class_grades(self):
        """Simple preview of students grades"""
        # Protection against no grades inputted
        if len(self.class_grades) == 0:
            self.message = "No grades inputted yet!"
        else:
            message = f'Current Grades:'
            for key in self.class_grades:
                message = message + f'\n{self.class_grades[key]}'
            self.message = message

    def exit(self):
        """exits application"""
        self.message = "Have a nice day!"
        self.continue_execution = False
    
    def help(self):
        """Help comments"""
        # Add this in towards the end?
        self.message = "PLACE HOLDER"