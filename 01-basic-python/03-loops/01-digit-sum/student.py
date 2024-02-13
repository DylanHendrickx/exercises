# Write your code here

def digit_sum(n):
    i = n
    i = sum(int(digit) for digit in str(n))
    return i

def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10