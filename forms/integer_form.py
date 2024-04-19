"""integer form to check user input"""
import numbers

class IntegerForm():

    def check_integer(self, input):
        # Check if its a string or numbers type
        if not isinstance(input, str):
            return None
        else:
            try:
                input = int(input)
                # Checks if greater than 0
                if input >= 0:
                    return input
            except ValueError:
                return None
            