print("Masukkan kecepatan dan jarak tempuh!")
kecepatan = float(input("Kecepatan : ")) # "3.4" -> float("3.4")
jarak = float(input("Jarak : ")) # int(..), str()
#casting : mengubah tipe data str > int atau str > float
waktu = jarak/kecepatan
print("Waktu :", waktu)