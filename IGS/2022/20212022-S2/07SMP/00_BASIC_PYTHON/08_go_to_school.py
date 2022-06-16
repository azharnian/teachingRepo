# hadShower = True
# hadShower = False
#boolean data type : True False


# rules pergi ke sekolah
# 1. Sudah Mandi dan bawa tas
# 2. bawa Bekal atau bawa uang saku
# 3. bukan hari minggu

hadShower = True
hasBackpack = True

hasMeal = True
hasMoney = False

isSunday = False

# operator logic

shouldGoToSchool = (hadShower and hasBackpack) and (hasMeal or hasMoney) and (not isSunday)

print(shouldGoToSchool)





