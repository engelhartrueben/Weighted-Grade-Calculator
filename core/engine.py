from forms.name_form import NameForm
from forms.string_form import StringForm

class AppEngine:
    def __init__(self, grade_item=None):
        self.message = None
        self.continue_execution = True
        self.grade_item = grade_item
        self.student_name = None
        self.class_name = None

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
    
    def get_class_name(self):
        """sets class name for this session"""
        prompt = "Enter Class Name: "
        while not self.class_name:
            cmd = input(prompt)
            class_name = StringForm.check_string(self, cmd)
            if not class_name:
                # Not entirely neccessary due to how
                # check_string works. Not many things to 
                # throw it off. Oh well. At least it formats
                print("Invalid Class Name!")
            else:
                self.class_name = class_name
            
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