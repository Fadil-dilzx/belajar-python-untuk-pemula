##Menjalankan program Python pertama kali##
print("Hello dari Python!")

##Vaiable Dan tipe data##
nama = "Fadil"
print(type(nama))  
umur = 17
print(type(umur)) 

nama = "Fadil"
umur = 17
tinggi = 170.5
is_active = True

print(nama)     
print(umur)      
print(tinggi)    
print(is_active) 

###Operator##
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)      # True
print("pisang" not in buah) # True

##Kondisi If Else pada Python##
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")
# Output: B

###Perulangan pada Python##
count = 0

while count < 5:
    print("Hitung:", count)
    count += 1

for i in range(1, 6):
    if i == 3:
        continue  # lewati angka 3
    if i == 5:
        break     # hentikan loop saat i == 5
    print(i)

##Lists dan Dictionaries##
# Membuat list
buah = ["apel", "jeruk", "mangga"]

# Akses elemen
print(buah[0])   # apel

# Menambah elemen
buah.append("pisang")

# Mengubah elemen
buah[1] = "anggur"

# Menghapus elemen
buah.remove("mangga")

print(buah)

# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

##Functions##
def sapa():
    print("Halo, selamat datang di Python!")

# Memanggil function
sapa()

def sapa_nama(nama):
    print(f"Halo {nama}, semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Siti")

def tambah(a, b):
    return a + b

hasil = tambah(5, 7)
print("Hasil penjumlahan:", hasil)

##Class dan Object##
# Membuat class
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

# Membuat object dari class
mhs1 = Mahasiswa("Fadil", "Informatika")
mhs2 = Mahasiswa("F", "RPL")

# Memanggil method
mhs1.sapa()
mhs2.sapa()

class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())
print("Keliling:", pp.keliling())
