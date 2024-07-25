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

class Application:
    def __init__(self):
        self.__orderbook = OrderBook()
    def helper(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer\n")

    def add_order(self):
        try:
            description = input("description: ")
            prowork = input("programmer and workload estimate: ")
            prowork = prowork.split(" ")
            self.__orderbook.add_order(description, prowork[0], int(prowork[1]))
            print("added!")

        except:
            print("erroneous input")

    
    def list_finished(self):
        finished = self.__orderbook.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for task in finished:
                print(task)

    def list_unfinished(self):
        unfinished = self.__orderbook.unfinished_orders()
        if len(unfinished) == 0:
            print("no unfinished tasks")
        else:
            for task in unfinished:
                print(task)

    def mark_finish(self):
        try:
            id = int(input("id: "))
            self.__orderbook.mark_finished(id)
            print("marked as finished")
        except:
            print("erroneous input")

    def list_programmers(self):
        lists = self.__orderbook.programmers()
        for pro in lists:
            print(pro)

    def status(self):
        
        try:
            pro = input("programmer: ")
            # (finished, unfinished, fhours, ufhours)
            tuplelist = self.__orderbook.status_of_programmer(pro)
            print(f"tasks: finished {tuplelist[0]} not finished {tuplelist[1]}, hours: done {tuplelist[2]} scheduled {tuplelist[3]}")
        except:
            print("erroneous input")
    
    def execute(self):
        self.helper()
        while True:
            command = input("command: ")
            if command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished()

            elif command == "3":
                self.list_unfinished()

            elif command == "4":
                self.mark_finish()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.status()
            elif command == "0":
                break

app = Application()

app.execute()