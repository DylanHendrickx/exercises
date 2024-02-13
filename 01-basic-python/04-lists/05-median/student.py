# Write your code here
def median(ns):
    ns.sort()
    if ((len(ns) -1) % 2) == 0:
        return ns[(len(ns)//2)]
    else:
        return (ns[((len(ns)-1)//2)]+ ns[((len(ns)+1)//2)]) /2
    