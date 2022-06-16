print("Masukkan kecepatan dan jarak tempuh.\n")
kecepatan = input("Kecepatan = ") #str / string 100 m/s
jarak = input("Jarak = ") # 10 m
# casting data type - > konversi tipe data
# str -> int() str -> float() int/float - > str()
waktu = float(jarak)/float(kecepatan)
print(f"\nWaktu = {waktu}.")
