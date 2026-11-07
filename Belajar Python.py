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
count = 0

while count < 5:
    print("Hitung:", count)
    count += 1
