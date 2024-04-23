"""Float form to check user input is flaot"""

class FloatForm:
    def check_float(self, input):
        # Check if its a string type
        if not isinstance(input, str):
            return None
        else:
            try:
                input = float(input)
                # Checks if greater than 0
                if input >= 0:
                    return input
            except ValueError:
                return None
            