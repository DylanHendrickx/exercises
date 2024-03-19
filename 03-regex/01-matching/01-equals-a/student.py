# Write your code here
import re;

def equals_a(string):
    correct_string = r'a'
    if re.fullmatch(correct_string, string):
        return True
    return False
    