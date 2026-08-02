todo_task=[]                #empty list

def add_task():             #Function to ADD TASkS
    task=input("Enter a Task: ")
    todo_task.append({"Task": task, "Status": "Pending"})
    print("\n Task Added Successfully ")
    print("\n")

def view_task():            #Function to View TAsks
    
    print("\n=======Your To-Do-List=======")
    if len(todo_task)==0:
        print("No pending Task..")
    else:
        for index,task in enumerate(todo_task,1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

def remove_task():          #Functions to Remove Tasks
    if len(todo_task)==0:
        print("List is Empty...")
        print("\n")

    else:
        try:
            search=int(input("Enter the task number you want to remove: "))-1
            if 0<=search<len(todo_task):
                removed_task=todo_task.pop(search)
                print(f"\nTask removed : {removed_task['Task']}")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("Please Enter a Valid Task Number. ")
    print("\n")


def mark_done_task():           #Function to mark Tasks as done
    if len(todo_task)==0:
        print("List is empty...")
        print("\n")
        
    else:
        try:
            search=int(input("Enter the task number you want to mark as done: "))-1
            if 0<=search<len(todo_task):
                todo_task[search]['Status']='Done'
                print(f"\nTask {todo_task[search]['Task']} has been marked as done ")
            else:
                print("Invalid Task Number \n")
        except ValueError:
                print("Please Enter a Valid Task Number. ")
    print("\n")
    
    



def display_menu():

    print("====== MENU FOR TO-DO-LIST ======")


    print("1. Add Task ")
    print("2. View Task ")
    print("3. Remove Task ")
    print("4. Mark the Task as Done")
    print("5. Exit")

while True:
    
    display_menu()
    try:
        choice = int(input("Choose what task you want to perform (1-5): "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        remove_task()
    elif choice==4:
        mark_done_task()
    elif choice==5:
        print("Program Exited!")
        break
    else:
        print("Invalid Input ")
    






