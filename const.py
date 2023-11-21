class myclass:

    a = 15
    b = 25

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)

one = myclass(50,50)
one.add()