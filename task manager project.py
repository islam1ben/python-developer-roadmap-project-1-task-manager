class InvalidStatusError(Exception):
    def __init__(self, message="Status must be either 'done', 'not done', or 'in progress'"):
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
        self.status='not done'
        self.status_positions = {'done','not done','in progress'}
        
        #task title can be null when initiated untill a text is affected to it 
        self.task_title=task_title

        

    def print_task (self):
        if  self.status=='not done':
            self.check_box_status=' '
        elif self.status=='done':
            self.check_box_status='*'
        elif self.status=='in progress':
            self.check_box_status='-'

        print(f"[{self.check_box_status}]  {self.task_title}")

    def update_task(self):
        while True:
            new_status = input('New status of the task: ')
            try:
                if new_status not in self.status_positions:
                    raise InvalidStatusError()
                self.status = new_status
                break  # Exit loop if status is valid
            except InvalidStatusError as e:
                print(e)  # Inform the user of the error


        new_task_title =input('new task title :')
        self.task_title=new_task_title

#task1=task('not done','give a gift to my brother')
#task1.print_task()




task1=task('do home work')
task1.print_task()
task1.update_task()
task1.print_task()