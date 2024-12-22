task=[]
def add_task():
    tasks=input("enter the task you want to add: ")
    task.append(tasks)
    print("Task added successfully!")
 
def view_task():
    print(task)
 
def remove_task():
   task.pop()

choice=int(input("Enter your choice:\n1.Add task \n2.View task \n3.Remove task "))
if choice==1:
    add_task()
if choice==2:
    view_task()
if choice==3:
    remove_task()
print(task)