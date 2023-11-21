class myclass:

    a = 15
    b = 25

    def msga(self):
        print("Message a")

    def msgb(self):
        print("message b")

    def msgc(self,i,j):
        print(i+j)

    def add(self):
        print(self.a+self.b)

    def newmethod(self,a,b):
        print(a+b)
one = myclass()
print(one.a)
print(one.b)
one.msga()
one.msgb()
one.msgc(15,25)
one.add()
one.newmethod(100,100)