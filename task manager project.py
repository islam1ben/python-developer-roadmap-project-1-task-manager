#creating task class 
#the task can be modified with its number in the shown list to avoid creating more variables and make it easier
class task:
    task_id=0
    check_box_status=None
    status_positions = {'done','not done','in progress'}
    def __init__ (self,status,task_title):
        
        #static variable for the task id the changes for every task
        task.task_id+=1
        self.id=task.task_id
        #make sure status is valid
        if status not in task.status_positions :
            raise ValueError('error , status must be either "done","not done" or "in progress"')
        self.status = 'not done'
        #task title can be null when initiated untill a text is affected to it 
        self.task_title=task_title

        

    def print_task (self):
        if  self.status=='not done':
            self.check_box_status=' '
        elif self.status=='done':
            self.check_box_status='*'
        elif self.status=='in progress':
            self.check_box_status='!'

        print(f"[{self.check_box_status}]  {self.task_title}")

#task1=task('not done','give a gift to my brother')
#task1.print_task()

class task_list :
    def __init__(self):
        self.tasks=[]

    def add_task(self,obj):
        if isinstance(obj,task):
            self.tasks.append(obj)
        else:    
            raise ValueError('you can only add a valid task formula to the tasks list')
    def delete_item(self,obj_id):
        self.tasks.id