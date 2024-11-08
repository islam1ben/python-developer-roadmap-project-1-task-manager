from task_manager_project import *
import os
import json

#function to clear the output every cycle
def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

#creating the task list
user_list = task_list()

#setting current list to empty list so that is satisfies the condition in line 31
user_list.current_list = []

#function of loading data from the file if existing if not returns an empty list
def load_data(user_list,data_file="data.json"):
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
            user_list.tasks = data.get("tasks")
            user_list.task_id_count = data.get("id_count")
    except FileNotFoundError:
        user_list.tasks
    


#function of saving data into the same file so that if its not existing it will create it
def save_data(user_list, filename="data.json"):
    data ={
        "tasks":user_list.tasks,
        "id_count": user_list.task_id_counter
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)



#loading the data from the file
load_data(user_list)

while True :
    #if list is empty sets it to the main list 
    if user_list.current_list==[None]:
        user_list.current_list=user_list.tasks
    else :pass

    #decoreting the output ,well ... kinda
    print('\t\t\tToDo List\n\n')
    user_list.print_list()
    print('\n\n')

    process = input('1-->add task\n2-->update task\n3-->remove task\n4-->show full list\n5-->show "todo" list\n6-->show "done" list\n7-->show "in progress" list\n8-->quite task manager\n')


    #creating an infinit loop only close if the user chose to 
    match process:
        case '1':
            user_list.add_task()


        case '2':
            #get the number of the task to update
            while True :
                task_num = int(input('type the number of the task you want to update in this list:'))
                if task_num<= user_list.i and task_num >0:
                    break
                else :
                    print ('task not found, try again')

            user_list.update_task(task_num)


        case '3':
            user_list.delete_task()
        case '4':
            user_list.current_list= user_list.tasks
        case '5':
            user_list.current_list= [todo_task for todo_task in user_list.tasks if todo_task['status']=='todo']
        case '6':
            user_list.current_list= [done_task for done_task in user_list.tasks if done_task['status']=='done']
        case '7':
            user_list.current_list=  [todo_task for todo_task in user_list.tasks if todo_task['status']=='in progress']
        case '8':
            break
    clear_output()

save_data(user_list)

print('---your data has been saved---')
