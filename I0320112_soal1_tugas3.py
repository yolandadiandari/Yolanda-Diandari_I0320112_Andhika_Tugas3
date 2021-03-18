list= ['yukuri', 'moris', 'zanet', 'sekar', 'vizal', 'deny', 'zafira', 'bonang', 'riri', 'rana']

#Menampilkan list indeks 4,6,7
print("Nama Teman indeks 4 6 7 :", list[4], ",", list[6], ",", list[7])

#mengganti nama teman list 3,5,9
list[2] = "Vincen"
list[4] = "stepy"
list[8] = "raysa"
print(list)

#menambah nama teman
list.extend(['Sasa', 'Rara'])
print(list)

#menampilkan nama teman dalam perulangan
urutanlist = 0
for data in range (0,12):
    print(list[urutanlist])
    urutanlist = urutanlist + 1

#menampilkan panjang list
print(len(list))

