hadShower = False
hasBackpack = True
#and

hasLunch = True
hasMoney = False
#or

weekend = False
#not
shouldGoToSchool = (hadShower and hasBackpack) and (hasLunch or hasMoney) and (not weekend)

print(f"Go to school = {shouldGoToSchool}")

"""
operator logika (gerbang logika)
and, or, not

true and true = true
true and false = false
false and true = false
false and false = false
=> AND

true or true = true
true or false = true
false or true = true
false or false = false
=> OR

not true = false
not false = true
not
"""