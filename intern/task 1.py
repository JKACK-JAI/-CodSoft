#To-Do List

todo_list = []


def show_menu():
    print("\n ...Your ToDo List Menu...")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")


def add_task():
    add = input("Enter Your Task: ")
    todo_list.append(add)
    print("\n Your Task Added Succesfully:)!!")



def view_task():
    if not todo_list:
        print("Your ToDo List is Empty:(...")
    else:
        print("Your Tasks:")
        for idx, add in enumerate(todo_list, start=1):
            print(f"{idx}. {add}")


def delete_task():
    view_task()
    if todo_list:
        try:
            remove = int(input("Enter Your task number to delete: "))
            if 1 <= remove <= len(todo_list):
                removed = todo_list.pop(remove - 1)
                print("\n Your Task Deleted Succesfully:)!!")
            else:
                print("Invalid Number...please try Again:(")
        except ValueError:
            print("Enter a valid Task number.")



while True:
    show_menu()
    choice = (input("Ente Your choice (1-4): "))


    if choice == '1':
        print("\n You Have Selectec Option '1' ")
        add_task()
    elif choice == '2':
        print("\n You Have Selected Option '2' ")
        view_task()
    elif choice == '3':
        print("\n You Have Selected Option '3' ")
        delete_task()
    elif choice == '4':
        print("Your ToDo List Session haas been Closed")
        print("Thanks For Using this ToDo-List Application:)!!")
        break
    else:
        print("Imvalid Choice. Backtrack it...!!")