contacts = {}

def add_contacts():
    name = input("Enter student name: ")
    no = input("Enter student number: ")
    contacts[name] = no
    print(f"{name} added successfully")

def search_contacts():
    search = input("Enter name to search: ")
    if search in contacts:
        no = contacts[search]
        print(f"Found — Name: {search} Number: {no}")
    else:
        print("No contact found")

def delete_contacts():
    delete = input("Enter name to delete: ")
    if delete in contacts:
        del contacts[delete]
        print(f"{delete} deleted successfully")
    else:
        print("Contact not found")

def list_contacts():
    if not contacts:
        print("No contacts found")
        return
    for name, no in contacts.items():
        print(f"Name: {name} | Number: {no}")

def menu():
    while True:
        print("\nSelect an option")
        print("1. Add contact")
        print("2. Search")
        print("3. Delete contact")
        print("4. List all contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "5":
            print("Bye!")
            break
        elif choice == "1":
            add_contacts()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            list_contacts()
        else:
            print("Invalid input")

menu()
