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

        while True:
            # This will have to change.
            # No point in asking this once you get farther
            # into the grading process
            prompt = "What would you like to do: "
            cmd = input(prompt)
            self.execute_command(cmd)
            print(self.engine.message)
            self.engine.message = None
            # Exit logic
            if not self.engine.continue_execution:
                break

    def execute_command(self, cmd):
        if cmd in ('q', 'quit', 'exit'):
            self.engine.exit()
            # Maybe add logic to save current work.
            # tinyDB?
        elif cmd in ('-h', '-help', 'help'):
            # call on a preformatted help
            # message
            self.engine.help()
        elif cmd in ('a', 'add', 'add student'):
            self.engine.get_student_information()
        elif cmd in ('v', 'view', 'view grades'):
            print(self.engine.preview_class_grades())
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


