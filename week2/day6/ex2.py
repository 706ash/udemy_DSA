def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for i in items:
            file.write(i + "\n")

fruits = ["apple", "banana", "cherry"]
write_item_to_file("sample1.txt", fruits)

