"""String form to check user input is flaot"""

"""
FORMATTING IDEAS ---
Math        : Math
enGlIsh     : English
maTH 207    : Math 207
137 CS      : 137 CS
% soci 3033 : Soci 3033
poli sci 1  : Poli Sci 1 
"""

class StringForm():
    def check_string(self, input):
        # Check if its a string type
        if not isinstance(input, str):
            return None
        else:
            return input