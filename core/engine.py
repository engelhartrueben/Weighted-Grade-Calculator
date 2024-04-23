from forms.string_form import StringForm
from forms.integer_form import IntegerForm

class AppEngine:
    def __init__(self, grade_item=None):
        self.message = None
        self.continue_execution = True
        self.grade_item = grade_item
        self.class_name = None
        self.assignment_count = None
        self.quiz_count = None
        self.project_count = None
    
    def get_class_name(self):
        """sets class name for this session"""
        prompt = "Enter Class Name: "
        while not self.class_name:
            class_name = StringForm.check_string(self, input(prompt))
            if not class_name:
                # Not entirely neccessary due to how
                # check_string works. Not many things to 
                # throw it off. Oh well. At least it formats
                print("Invalid Class Name!")
            else:
                self.class_name = class_name
    
    def get_counts(self):
        """gets total amount of counts of"""
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
            
    def add_grade(self):
        pass

    def calculate_grade(self):
        pass

    def exit(self):
        """exits application"""
        self.message = "Have a nice day!"
        self.continue_execution = False
    
    def help(self):
        """Help comments"""
        # Add this in towards the end?
        self.message = "PLACE HOLDER"