

class AppEngine():
    def __init__(self, grade_item=None):
        self.message = None
        self.continue_execution = True
        self.grade_item = grade_item

    def add_grade(self):
        pass

    def calculate_grade(self):
        pass

    def exit(self):
        self.message = "Have a nice day!"
        self.continue_execution = False
    
    def help(self):
        """Help comments"""
        # Add this in towards the end?
        self.message = None