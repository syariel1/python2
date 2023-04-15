print(3*"-"," file reader ",3*"-")

file = open("file.txt",mode="r")
print(f"buka file : {file.readable()}")

print(file.read())

# print(file.readline, end="")
# print(file.readline, end="")

# print(f"file satu satu = {file.readlines()}")

print(f"apakah file sudah ditutup : {file.closed}")
file.close()
print(f"apakah file sudah ditutup : {file.closed}")

# menggunakan with 

print(3*"-"," file reader menggunakan with ",3*"-")
with open("file.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah ditutup : {file.closed}")

print(f"apakah file sudah ditutup : {file.closed}")