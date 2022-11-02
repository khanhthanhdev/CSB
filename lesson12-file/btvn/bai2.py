file_name = input("Input file name: ")

file = open(f"D:\\CSB\\lesson12-file\\btvn\\names.txt", "r")


if file_name == "names.txt":
    print("File content: ")
    read_file = file.read()
    print(read_file)
elif file_name != "names.txt":
    print("File not found.")
