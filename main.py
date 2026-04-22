print("Welcome to the Contacts!")
contacts={}
def addcontact(contacts):
    name=input("Enter the name : ")
    mob_num=int(input("Enter the number :"))
    if name in contacts:
        contacts[name].append(mob_num)
    else:
        contacts[name] = [mob_num]
    print("Contact Added Successfully...")

def viewcontact(contacts):
    if not contacts:
        print("No Contacts Available...")
        return

    for name, numbers in contacts.items():
        print(f"{name} | Mobile Numbers: ", end="")
        for num in numbers:
            print(num, end=", ")
        print()

def search(contacts):
    searches = input("Enter the name: ")

    if searches in contacts:
        numbers = contacts[searches]
        print(f"Name: {searches} |Mobile Number : ", end="")
        for num in numbers:
            print(num, end=" ")
        print()
    else:
        print("Contact not found...")

def delete_contact(contacts):
    delete = input("Enter the name you want to DELETE: ")

    if delete in contacts:
        numbers = contacts[delete]
        if len(numbers) == 1:
            del contacts[delete]
            print("Contact deleted successfully...")

        else:
            print(f"Numbers for {delete}:")
            for i, num in enumerate(numbers, start=1):
                print(f"{i}. {num}")

            choice = input("Delete (1) specific number OR (2) full contact? ")

            if choice == "1":
                index = int(input("Enter the number index to delete: ")) - 1

                if 0 <= index < len(numbers):
                    removed = numbers.pop(index)
                    print(f"{removed} deleted successfully.")
                    if not numbers:
                        del contacts[delete]

                else:
                    print("Invalid index.")

            elif choice == "2":
                del contacts[delete]
                print("Contact deleted successfully...")

            else:
                print("Invalid choice.")

    else:
        print("Contact not found...")

while True:
    print("1. ADD Contact.")
    print("2. View Contact .")
    print("3. Search Contact .")
    print("4. Delete Contact .")
    print("5. Exit .")
    choice=int(input("Enter your choice : "))
    if choice==1:
        addcontact(contacts)
        
    elif choice ==2:
        viewcontact(contacts)

    elif choice ==3:
        search(contacts)

    elif choice ==4:
        delete_contact(contacts)

    elif choice==5:
        print("Exiting the code...")
        break
    
    else:
        print("Enter a valid Choice From the given menu...")

