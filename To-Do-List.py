
def display_menu():
    print("====== TO-DO-LIST ======")


    print("1. Add Task ")
    print("2. View Task ")
    print("3. Update Tsk ")
    print("4. Remove Task ")
    print("5. Exit")

while True:
    display_menu()
    choice=int(input("Choose what task you want to perform (1-5): "))
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        update_task()
    elif choice==4:
        remove_task()
    elif choice==5:
        print("Program Exited!")
        break
    else:
        print("Invalid Input ")







