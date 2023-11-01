class Contact:
    def __init__(self, name,phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

def add_contact(contacts, name, phone, email, address):
    new_contact = Contact(name, phone, email, address)
    contacts[name] = new_contact

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, contact in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print("")

def search_contact(contacts, query):
    matching_contacts = {}
    for name, contact in contacts.items():
        if query.lower() in name.lower() or query in contact.phone:
            matching_contacts[name] = contact
    return matching_contacts

def update_contact(contacts, name, phone, email, address):
    if name in contacts:
        contact = contacts[name]
        contact.phone = phone
        contact.email = email
        contact.address = address
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
    else:
        print(f"Contact {name} not found.")

def main():
    print("Contact Management System")
    contacts = {}

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            add_contact(contacts, name, phone, email, address)
            print("Contact added successfully.")

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            query = input("Enter a name or phone number to search: ")
            matching_contacts = search_contact(contacts, query)
            view_contacts(matching_contacts)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone = input("New phone: ")
            email = input("New email: ")
            address = input("New address: ")
            update_contact(contacts, name, phone, email, address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)

        elif choice == "6":
            break

if __name__ == "__main__":
    main()
