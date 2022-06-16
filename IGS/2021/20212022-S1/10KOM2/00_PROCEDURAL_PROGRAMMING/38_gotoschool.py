

hadShower = True
hasBackpack = True
# True

hasMeal = True
hasMoney = False
# True

isSunday = False
# True

shoudGoToSchool = not isSunday and (hadShower and hasBackpack) and (hasMeal or hasMoney)
# True and True and True = True
print(shoudGoToSchool)