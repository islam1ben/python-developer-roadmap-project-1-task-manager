import time 

#the task list is a list of dictionaries each one contains task properies

class task_list :
    current_list=[]
    def __init__(self):
        self.tasks=[]
    #the id counter job is 
    task_id_counter=1

    #adding task by giving it the creation time and default "todo" status
    def add_task(self):
       temp_title = input ('enter your task :')
       temp_task= {'id':self.task_id_counter,'status':'todo','title':temp_title,'creation time':time.asctime(),'update time':None}
       self.tasks.append(temp_task)
       self.task_id_counter+=1

    #deleting the task using its number in the list
    def delete_task (self):
        while True :
            task_num = int(input('type the number of the task you want to delete in this list:'))
            if task_num<= self.i and task_num >0:
                break
            else :
                print ('task not found, try again')

        #basically removing the task by updating the list because i don't know any other way
        id_to_remove = self.current_list[task_num-1]['id']
        self.tasks=[item for item in self.tasks if item['id'] != id_to_remove]
        self.current_list=self.tasks


    def print_list(self):
        self.i=1
        for item in self.current_list:
            print(f'{self.i}',end='.')
            #changing the checkbox of each task be=ased on its status
            if  self.current_list[self.i -1]['status']=='todo':
                check_box_status=' '
            elif self.current_list[self.i -1]['status']=='done':
                check_box_status='*'
            elif self.current_list[self.i -1]['status']=='in progress':
                check_box_status='~'

            print(f"[{check_box_status}]  {self.current_list[self.i -1]['title']}")
            self.i+=1

    #changing the status of the task based on the used input and also giving it the update time 
    def update_task(self,task_num):
        operation =input('1-->done    2-->in progress    3-->todo\n')
        self.current_list[task_num-1]['update time']=time.asctime()
        match(operation):
            case '1':
                self.current_list[task_num-1]['status']='done'
            case '2':
                self.current_list[task_num-1]['status']='in progress'
            case '3':
                self.current_list[task_num-1]['status']='todo'
            case _:
                print('error!, invalid input')
