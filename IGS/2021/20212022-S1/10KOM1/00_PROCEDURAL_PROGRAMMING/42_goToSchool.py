
hadShower = True
hasBackpack = True
#or

hasMeal = True
hasMoney = False
#or

sunday = False

shouldGoToSchool = not sunday and (hadShower and hasBackpack) and (hasMeal or hasMoney)
#True and True and True

print(shouldGoToSchool)
