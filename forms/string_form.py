"""String form to check user input is flaot"""

class StringForm():
    def check_string(self, input):
        # Check if its a string type
        if not isinstance(input, str):
            return None
        else:
            return input