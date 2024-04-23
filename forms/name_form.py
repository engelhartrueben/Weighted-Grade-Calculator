"""Form to validate name"""

class NameForm:
    def check_name(self, input):
        if not isinstance(input, str) or len(input.strip()) == 0:
            return None
        else:
            input = input.strip().split(' ')
            while "" in input:
                input.remove("")
            if len(input) > 0 and len(input) <= 3:
                capitalizedName = []
                for part in input:
                    part = part.strip()
                    # '*' is an unpack method. Super cool
                    # EXAMPLE w/ .lower() : ["rUBY"] => ["r", "u", "b", "y"]
                    part = [*part.lower()]

                    # Capatalizes the first letter of each part of the name
                    part[0] = part[0].upper()

                    # Appends to create initials and capitalized name
                    capitalizedName.append("".join(part))
                return " ".join(capitalizedName)
            else:
                return None