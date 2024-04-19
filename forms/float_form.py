"""Float form to check user input is flaot"""

class FloatForm():
    def check_integer(self, input):
        # Check if its a string type
        if not isinstance(input, str):
            return None
        else:
            input = input.strip()
            try:
                float = float(input)
                return float
            except ValueError:
                return None
            