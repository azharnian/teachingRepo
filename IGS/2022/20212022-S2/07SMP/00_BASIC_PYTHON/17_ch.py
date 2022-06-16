"""
Buat 3 dictionary yg menampilkan orang yg berbeda.
simpan ketiga orang tersebut di dalam sebuah list
Untuk informasi yg disimpan adalah
key : username,
value :
 1. nama depan
 2. nama belakang
 3. hobi
"""


people = [
	{
        "frontname" : "Andi",
        "lastname" : "Siregar",
        "hobby" : "Memancing"
    },
    {
        "frontname" : "Budi",
        "lastname" : "Susilo",
        "hobby" : "Melukis"
    },
    {
        "frontname" : "Cindy",
        "lastname" : "Hutapea",
        "hobby" : "Memasak"
    }
]

for person in people:
    for key, value in person.items():
        print(f"{key}\t:{value}")
    print()






