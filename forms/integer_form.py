"""integer form to check user input"""

class IntegerForm:
    def check_integer(self, input):
        # Check if its a string or numbers type
        if not isinstance(input, str):
            return None
        else:
            try:
                if int(input) == float(input) and int(input) >= 0:
                    return int(input)
            except ValueError:
                return None
            