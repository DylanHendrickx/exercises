
def take_while(xs, condition):
    good_ones = []
    bad_ones = []
    for x in xs:
        if condition(x) == True:
            good_ones.append(x)
        else:
            bad_ones.append(x)
    return (good_ones, bad_ones)