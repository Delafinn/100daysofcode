with open("../../../Desktop/mytext.txt") as file:

    contents = file.read()
    print(contents)





with open("new_text.txt", mode = "ab") as file:
    file.write("hello world!")
    contents = file.read()
    print(contents)
