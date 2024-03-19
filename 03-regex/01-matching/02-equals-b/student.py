# Write your code here
import re;

def equals_b(string):
    correct_string = r'b'
    if re.fullmatch(correct_string, string):
        return True
    return False