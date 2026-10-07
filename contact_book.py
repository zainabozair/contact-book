# Contact Book Application

# Dictionary used to store contact names and phone numbers
contacts = {}

def add_contact(contacts):
    name = input("Enter conatct name: ")

    if name == "":
        print("Name connot be empty")
        return

    if name in contacts:
        print("contact already exists.")
        return

    phone = input("Enter phone number: ")

    if not phone.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return

    contacts[name] = phone
    print("contact added successfully")

# Displays all contacts
def view_contacts(contacts):
    if not contacts:
        print("Contact list is empty.")
        return
    
    for name, phone in contacts.items():
        print(name, ":", phone)

# Searches for a contact by full or partial name
def search_contact(contacts):
    search_name = input("Enter contact name to search: ")

    found = False

    for name,phone in contacts.items():
        if search_name.lower() in name.lower():
            print(name, ":", phone)
            found = True

    if not found:
        print("Contact not found.")

# Deletes a contact
def delete_contact(contacts):
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("contact deleted.")
    else:
        print("contact not found")

# Main menu
while True:
    print("\nContact Book Menu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")    

    try:
        choice = int(input("Enter your choice 1-5: "))

        if choice == 1:
            add_contact(contacts)
        
        elif choice == 2:
            view_contacts(contacts)

        elif choice == 3:
            search_contact(contacts)

        elif choice == 4:
            delete_contact(contacts)

        elif choice == 5:
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")







