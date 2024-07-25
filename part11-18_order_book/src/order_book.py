# Write your solution here:

class Task:
    count = 1
    def __init__(self, description, programmer, workload):
        self.__is_finished = False
        self.__id = Task.count
        Task.count+=1

        self.__description = description
        self.__programmer = programmer
        self.__workload = workload
    
    @property
    def id(self):
        return self.__id
    
    @property
    def description(self):
        return self.__description
    
    @property
    def programmer(self):
        return self.__programmer
    
    @property
    def workload(self):
        return self.__workload
    
    def is_finished(self):
        return self.__is_finished
    
    def mark_finished(self):
        self.__is_finished = True
    
    def __str__(self):
        finish = "FINISHED" if self.__is_finished else "NOT FINISHED"
        return f"{self.__id}: {self.__description} ({self.__workload} hours), programmer {self.__programmer} {finish}"
    


class OrderBook:
    def __init__(self):
        self.__orders = []
    
    def add_order(self, description, programmer, workload):
        self.__orders.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.__orders
    
    def programmers(self):
        return list(set([task.programmer for task in self.all_orders()]))
    
    def mark_finished(self, id:int):
        task = None
        for tk in self.__orders:
            if tk.id == id:
                task = tk
                break
        if task == None:
            raise ValueError
        task.mark_finished()
    
    def finished_orders(self):
        return [task for task in self.__orders if task.is_finished() == True]
    
    def unfinished_orders(self):
        return [task for task in self.__orders if task.is_finished() == False]
    
    def status_of_programmer(self, programmer:str):
        finished = 0
        unfinished = 0
        fhours = 0
        ufhours =0
        flag = None
        for task in self.__orders:
            if task.programmer == programmer:
                flag = programmer
                if task.is_finished():
                    finished+=1
                    fhours += task.workload
                else:
                    unfinished+=1
                    ufhours += task.workload
        if flag == None:
            raise ValueError
        return (finished, unfinished, fhours, ufhours)

