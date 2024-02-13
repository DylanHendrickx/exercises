# Write your code here
import math
def cakes(eggs, butter, flour):
    TEggs = math.floor(eggs/5)
    TButter = math.floor(butter/250)
    TFlour = math.floor(flour/250)

    return min(TEggs, TButter, TFlour)
