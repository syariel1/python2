# contoh sederhana
input_user = int(input("masukan angka pembagi :"))
try:
    hasil = 10/input_user
    print(f"hasil : {hasil}")
except:
    print("input tidak boleh 0 ")

# contoh program aplikasi 
while(True):
    input_user = int(input("masukan angka pembagi :"))
    try:
        hasil = 10/input_user
        print(f"hasil : {hasil}")
        isDone = input("apakah anda ingin melanjutkan (y/n)? ")
        if isDone == "n" or "N":
            break
    except:
        print("hasil tidak boleh 0")

print("akhir dari program")

# contoh program aplikasi 2
try:
    with open("data1.txt","r") as file :
        print(file.read())
except: 
    print("membuat file baru")
    with open("data1.txt","w",encoding="utf-8") as file :
        file.write("file baru")
print("akhir dari program 2")


# membuat exception sendiri

from numbers import Number
def tambah (a,b):
    if not isinstance (a,Number) or not isinstance(b,Number) :
        raise "input harus angka"
    return a+b

print(tambah(5,5))

angka = 0
# try:
#     hitung = 10/angka
# except Exception as error_message:
#     print(error_message)

try:
    hitung = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)

