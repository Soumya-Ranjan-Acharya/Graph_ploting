with open("sonu.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")

with open("sonu.txt", "r") as file:
    print(file.read())

#r+ is used to read and write the file
# a+ is used to append and read the file
# w+ is used to write and read the file