# Write your code here

def includes(xs, ys):
    if any(elem in ys for elem in xs) == True:
        return True
    if ys == []:
        return True
    return False



#There's an all() and any() function to do this. To check if big contains ALL elements in small

#result = all(elem in big for elem in small)
#To check if small contains ANY elements in big

#result = any(elem in big for elem in small)
#the variable result would be boolean (TRUE/FALSE).
