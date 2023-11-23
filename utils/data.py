
Data = 'database.txt'


def add_newbook():
    with open(Data, 'a') as file:
        name = input("Enter name of the book")
        author = input("Enter name of the author")
        file.write(f"{name}#{author}#False\n")


def list_books():
    with open(Data, 'r') as file:
        data = [line.strip().split("#") for line in file.readlines()]
    for i in data:
        print(f"{i[0]} written by {i[1]} is read : {i[2]}")


def mark_read():
    a = input("Enter the book you want to be marked read : ")
    with open(Data, 'r') as file:
        data = [line.strip().split('#') for line in file.readlines()]

    for i in data:
        if i[0] == a:
            i[2] = 'True'
            break
    else:
        print("Book doesn't exist")
    with open(Data, 'w') as file:
        for i in data:
            file.write(f"{i[0]}#{i[1]}#{i[2]}\n")


def del_book():
    a = input("Enter the book you want to Delete : ")
    with open(Data, 'r') as file:
        data = [line.strip().split('#') for line in file.readlines()]
    for i in data:
        if a == i[0]:
            data.remove(i)
            break
    else:
        print("Book doesn't exist")
    with open(Data, 'w') as file:
        for i in data:
            file.write(f"{i[0]}#{i[1]}#{i[2]}\n")
