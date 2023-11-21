#convert user arguments to class arguments without using constructor

class myclass:

    a=50
    b=50


    def task(self,a,b):
        self.a = a
        self.b = b
        print(self.a+self.b)

    def add(self):
        print(self.a+self.b)

one = myclass()
one.task(150,150)
one.add()

