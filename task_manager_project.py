class InvalidStatusError(Exception):
    def __init__(self, message="Status must be either 'done', 'todo', or 'in progress'"):
        self.message = message
        super().__init__(self.message)

#creating task class 

#the task can be modified with its number in the shown list to avoid creating more variables and make it easier
class task:
    task_id_counter=0
    

    def __init__ (self,task_title):
        
        #static variable for the task id the changes for every task
        task.task_id_counter+=1
        self.id=task.task_id_counter
        #make sure status is valid
        self.check_box_status=None
        self.status='todo'
        self.status_positions = ['done','todo','in progress']
        
        #task title can be null when initiated untill a text is affected to it 
        self.task_title=task_title

        

    def print_task (self):
        if  self.status=='todo':
            self.check_box_status=' '
        elif self.status=='done':
            self.check_box_status='*'
        elif self.status=='in progress':
            self.check_box_status='-'

        print(f"[{self.check_box_status}]  {self.task_title}")

    def update_task(self):

        while True :
            status_updater = input('do you want to change task status?\nY--> yes   N-->no').upper()
            if status_updater=='Y':
            
                while True:
                    new_status = input('New status of the task: ')
                    try:    
                        if new_status not in self.status_positions:
                            raise InvalidStatusError()
                        self.status = new_status
                        break  # Exit loop if status is valid
                    except InvalidStatusError as e:
                        print(e)  # Inform the user of the error
                break        
            elif status_updater == 'N':
                break

            else :
                print('invalid input')

        

        while True:
            title_updater = input('do you waant to chane the task\' title?\nY-->yes  N-->no').upper()
            if title_updater=='Y':
                new_task_title =input('new task title :')
                self.task_title=new_task_title
                break
            elif title_updater=='N':
                break
            else :
                print('invalid input please try again')



class task_list :
    current_list=[]
    def __init__(self):
        self.tasks=[]

        self.list_of_done_tasks = [done_task for done_task in self.tasks if done_task.status=='done']
        self.list_of_todo_tasks = [todo_task for todo_task in self.tasks if todo_task.status=='todo']
        self.list_of_in_progress_tasks = [in_progress_task for in_progress_task in self.tasks if in_progress_task.status=='in progress']


    def add_task(self):
       temp_title = input ('enter your task :')
       temp_task= task(temp_title)
       self.tasks.append(temp_task )
    


    def delete_task (self):
        while True :
            task_num = int(input('type the number of the task you want to delete in this list:'))
            if task_num<= self.i and task_num >0:
                break
            else :
                print ('task not found, try again')


        id_to_remove = self.current_list[task_num-1].id
        self.tasks=[item for item in self.tasks if item.id != id_to_remove]


    def print_list(self):
        self.i=1
        for item in self.current_list:
            print(f'{self.i}',end='.')
            self.i+=1
            item.print_task()


