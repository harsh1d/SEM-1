# f = open("C:\\Users\\ndevr\\Desktop\\PYTHON\\file.txt", "r")
# print(f.read())

# print("")

# f = open("C:\\Users\\ndevr\\Desktop\\PYTHON\\file.txt", "w")
# print(f.write("Well Done"))

f = open("C:\\Users\\ndevr\\Desktop\\PYTHON\\file.txt", "r")
# print(f.read().capitalize())
print(f.read().upper())
# print(f.read().title())
f = open("C:\\Users\\ndevr\\Desktop\\PYTHON\\file.txt", "w+")
b = f.readlines()
name=''
for i in b:
    i.upper()
    name = name+i

f.write(name)
    