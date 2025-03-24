def todo():
    print("""To do list
          1.Add a task
          2.View all tasks
          3.Delete a task
          4.Exit""")
todo()
tasks=[]
while True:
    choice = int(input("Enter your choice 1 or 2 or 3 or 4: "))
    if choice == 1:
        task = input("Enter the task:").lower()
        tasks.append(task)
    elif choice == 2:
        print(tasks)
    elif choice == 3:
        task = input("Enter task to delete: ").lower()
        tasks.remove(task)
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")
    next = input("Do you want to continue y/n: ")
    if next == "y" or next =="Y":
        continue
    else:
        break
