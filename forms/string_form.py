"""String form to check user input is flaot"""

class StringForm():
    def check_string(self, input):
        # Check if its a string type
        if not isinstance(input, str):
            return None
        else:
            input = input.split(' ')
            final_input = []
            for spaces in input:
                if len(spaces) >= 3:
                    spaces = [*spaces.lower()]
                    spaces[0] = spaces[0].upper()
                    final_input.append("".join(spaces))
                else:
                    final_input.append("".join([*spaces.upper()]))
            return " ".join(final_input)