"""integer form to check user input"""

class IntegerForm():
    def check_integer(self, input):
        # Check if its a string type
        if not isinstance(input, str):
            return None
        else:
            input = input.strip()
            try:
                int = int(input)
            except ValueError:
                return None
            