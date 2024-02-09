class Task:
    def getstring(self):
        self.n = input()

    def printstring(self):
        print(self.n.upper())

my_task = Task()

my_task.getstring()
my_task.printstring()
