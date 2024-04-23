from core.engine import AppEngine

class App:
    def __init__(self, grade_items=None):
        self.engine = AppEngine(grade_items)

    def run(self):
        """rotatin function for user input"""
        # Add in intial welcomd message here
        print("Welcome to Weighted Grade Calculator!"/
              " At any time, type '-h' for help!")
        # Would like to add a basic 2d render
        while True:
            prompt = "one thing or another"
            cmd = input(prompt)
            self.execute_command(cmd)
            
            # Exit logic
            if not self.engine.continue_execution:
                break

    def execute_command(self, cmd):
        if cmd in ('q', 'quit', 'exit'):
            self.engine.exit()
            # Maybe add logic to save current work.
            # tinyDB?
        elif cmd in ('-h', '-help'):
            # call on a preformatted help
            # message
            self.engine.help()

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
    engine = AppEngine(grade_item=grade_items)


