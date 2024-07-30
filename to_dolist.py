# a simple to do list program
from datetime import date
tasks = []
status =[]
current_date = date.today()

filename1 = 'tasks.txt'
filename2='status.txt'
print("####To do list program###")
print("####1 to enter the list of your tasks.###")
print("####2 to enter the status of each task.###")
mychoice = "Enter your choice"
choice = int(input(mychoice+">"))

#list your daily tasks
if choice ==1:
    count = 0
    myfile = open(filename1,'w')
    print("\n Enter your tasks.")
    print("Enter 'exit' to stop")
    while True:
        yourtask = input("Enter your task"+ str(len(tasks)+1)+":")
        if yourtask.lower()=='exit':
            print("You can come next and fill their status")
            break
        else:      
            tasks.append(yourtask)

    #write the date and tasks on task.txt file
    myfile.write("Date:"+str(current_date))
    myfile.write("\n"+str(tasks))   

#list the status of your tasks     
elif choice ==2:
    myfile = open(filename1,'r')
    list_str = myfile.readlines()
    tasklist = eval(list_str[1])
    count = 0
    print("\n Enter status of your tasks as complete/incomplete.")
    print("Enter 'exit' to stop")
    while True:
        yourstatus = input("Status of task "+tasklist[count]+":")
        if yourstatus.lower()=='exit':
            break
        else:
            status.append(yourstatus)  
            count+=1
            if count == len(tasklist): break
    
    while count<len(tasklist):
        status.append("unspecified")
        count+=1 

    myfile=open(filename2,'w')
    myfile.write(str(status))
#if other values are entered   
else:
    print("Enter the right choice")