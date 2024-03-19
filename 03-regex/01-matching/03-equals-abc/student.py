# Write your code here
import re;

def equals_abc(string):
    correct_string = r'abc'
    if re.fullmatch(correct_string, string):
        return True
    return False