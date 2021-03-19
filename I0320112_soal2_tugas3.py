dict = {'Nama': ['Yolanda Diandari'],
        'Hobi': ['Membaca','Menulis','Bernyanyi'],
        'Sosial media': ['IG : @yolan.dn','Line : yolan.dn','Quora : Gaia Mentari'],
        'Lagu kesukaan' : ['Hericane','Malibu Nights','All I Want'],
        'Makanan favorit' : ['Sup ayam mama','Dimsum','Pasta']}

print(dict)

#mengubah salah satu hobi dan sosial media
dict['Hobi'][1] = ('Netflixan')
dict['Sosial media'][1] = ('Twitter : thinkerbelle')

#menghapus 2 makanan favorit
del(dict)['Makanan favorit'][1:]

#menambahkan 1 hobi
dict['Hobi'].append('Kulineran')

print(dict)

