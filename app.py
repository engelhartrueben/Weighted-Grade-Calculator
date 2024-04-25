from core.engine import AppEngine

class App:
    def __init__(self, grade_items=None):
        self.engine = AppEngine(grade_items)

    def run(self):
        """rotating function for user input"""
        # Add in intial welcomd message here
        print("Welcome to Weighted Grade Calculator!"
              " At any time, type '-h' for help!\n")
        # Gets class name
        self.engine.get_class_name()
        # Gets counts of assignments, quizzes, and projects
        self.engine.get_counts()
        did_input_last_student = None

        while True:
            # This will have to change.
            # No point in asking this once you get farther
            # into the grading process
            last_student_logic = (did_input_last_student == None or did_input_last_student == True)
            # Grabs the length of the class grades
            if len(self.engine.class_grades) == 0 and did_input_last_student == None:
                prompt = "Would you like to add your first student? (y/n) "
            elif len(self.engine.class_grades) > 0 and last_student_logic:
                prompt = "Would you like to add another student? (y/n)"
            else:
                prompt = "what would you like to do? "
            cmd = input(prompt)
            if cmd in ('y'):
                did_input_last_student = True
            else:
                did_input_last_student = False
            self.execute_command(cmd)
            if self.engine.message is not None:
                print(self.engine.message)
            self.engine.message = None
            # Exit logic
            if not self.engine.continue_execution:
                break

    def execute_command(self, cmd):
        if cmd in ('-q', '-quit', '-exit'):
            self.engine.exit()
            # Maybe add logic to save current work.
            # tinyDB?
        elif cmd in ('-h', '-help', 'help'):
            # call on a preformatted help
            # message
            self.engine.help()
        elif cmd in ('y', 'add'):
            self.engine.get_student_information()
        elif cmd in ('v', 'view', 'view grades'):
            print(self.engine.preview_class_grades())
        elif cmd == ('change class name'):
            self.engine.get_class_name()
        # Do not include these three in help
        # Have to first build out funcitonality
        # to go back and add assignments to previous
        # students, if this was changed after any inputs
        # currently killing this command, but still cool
        elif cmd == ('change assignment amount') and len(self.engine.class_grades) == 0:
            self.engine.get_counts('Assignments')
        elif cmd == ('change quiz amount') and len(self.engine.class_grades) == 0:
            self.engine.get_counts('Quizzes')
        elif cmd == ('change project amount') and len(self.engine.class_grades) == 0:
            self.engine.get_counts('Projects')
        elif cmd == ('n'):
            # Cheeky pass to do nothing
            pass
        else:
            self.engine.message = f'"{cmd}" is not a valid command.\n'

if __name__ == '__main__':
    # Eventually would like this to be dynamic.
    # As in the user can customize based on their
    # class
    grade_items = [
        'Quizzes',
        'Projects',
        'Assignments',
        'Participation'
    ]
    app = App(grade_items)
    app.run()


