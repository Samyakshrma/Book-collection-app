from utils import data

User_choice = """
a --> add new books
b --> list all books
c --> mark books as read
d --> delete a book
q --> quit
Enter your choice here : """


def menu():
    print(User_choice)
    ch = input()
    while ch != 'q':
        if ch == 'a':
            data.add_newbook()
        elif ch == 'b':
            data.list_books()
        elif ch == 'c':
            data.mark_read()
        elif ch == 'd':
            data.del_book()
        else:
            print("Enter a valid choice\n\n")
        menu()


menu()
