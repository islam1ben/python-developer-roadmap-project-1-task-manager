from task_manager_project import *
import os
import json

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

user_list = task_list()

user_list.current_list = []

def load_data(data="data_file.json"):
    try:
        with open(data, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


user_list.tasks=load_data()

while True :
    if user_list.current_list==[]:
        user_list.current_list=user_list.tasks
    else :pass

    print('\t\t\tToDo List\n\n')
    user_list.print_list()
    print('\n\n')

    process = input('1-->add task\n2-->update task\n3-->remove task\n4-->show full list\n5-->show "todo" list\n6-->show "done" list\n7-->show "in progress" list\n8-->quite task manager\n')

    match process:
        case '1':
            user_list.add_task()
        case '2':
            while True :
                task_num = int(input('type the number of the task you want to update in this list:'))
                if task_num<= user_list.i and task_num >0:
                    break
                else :
                    print ('task not found, try again')

            user_list.current_list[task_num - 1].update_task()

        case '3':
            user_list.delete_task()
        case '4':
            user_list.current_list= user_list.tasks
        case '5':
            user_list.current_list=user_list.list_of_todo_tasks
        case '6':
            user_list.current_list=user_list.list_of_done_tasks
        case '7':
            user_list.current_list=user_list.list_of_in_progress_tasks
        case '8':
            break
    clear_output()

save_data(user_list.tasks)

print('---your data has been saved---')
#solve the problem of storing data