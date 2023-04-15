
# menggunakan write ("w")
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("isi data 1")
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("isi data 1.1")
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("isi data 1.2 (overwrite)")

# menggunakan append ("a")
with open("data_2.txt","w",encoding="utf-8") as file:
    file.write("isi data 2\n")
with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("isi data 2.2\n")
with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("isi data 2.3\n")

# menggunakan r+ ("r+")
with open("data_3.txt","w",encoding="utf-8") as file:
    file.write("isi data 3")
    
with open("data_3.txt","r+",encoding="utf-8") as file:
    file.write("isi data 3.1\n")
    file.write("isi data 3.2\n")
    file.write("isi data 3.3\n")

with open("data_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt","r+",encoding="utf-8") as file:
    file.write("mim data 3.1\n")
