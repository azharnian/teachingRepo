# messages.py

1. buat sebuah lists yg berisikan daftar pesan minimal 3
kemudian buat sebuah function di atasnya 'show_messages()'
yang fungsinya menampilkan tiap pesan satu persatu menggunakan
lists yg telah dibuat sebagai argumen.

2. ingin mengirim pesan, buatkan list kosong untuk menampung pesan
terkirim. 'sent_messages = []', kemudian buatkan sebuah function
di atas 'show_messages()' yang bertugas untuk memindahkan pesan
dari lists messages_list ke sent_messages. di dalam function dituliskan
tiap pesannya lagi diikuti kalimat, '....., msg sent!'. Dibuktikan dengan
print messages_list, dan sent_messages di paling bawah kode program.

3. buatkan messages_list sebagai arsip, sehingga tidak dihapus saat pop di function -> [:] letakkan dimana?

def send_messages(....):
	.....


def show_messages(messages_list):
	for .... :
		...
		...

messages_list = ["aaaa", "bbbb", "cccc"]
sent_messages = []
show_messages(messages_list)
send_messages(...,...)

print(messages_list) #kalau messages_list => ["aaaa", "bbbb", "cccc"]
print(sent_messages) #kalau sent_messages => ["cccc", "bbbb", "aaaa"]