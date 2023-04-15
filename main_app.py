

print(3*"-", " Membaca file ", 3*"-")

file = open("file.txt",mode="r")

print(f"read file {file.readable()}")

# baca seluruh file
print(file.read())

# baca per baris
# print(file.readline(), end='')
# print(file.readline(), end='')

# baca sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose? {file.closed}")
file.close()
print(f"apakah file sudah diclose? {file.closed}")

# teknik di python menggunakan with
print(3*"-", " Membaca file dengan with ", 3*"-")

with open ("file.txt",mode="r") as file :
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose? {file.closed}")

print(f"apakah file sudah diclose? {file.closed}")


