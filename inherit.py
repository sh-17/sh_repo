class parent:

    a = 10
    b = 20

    def parentmethod(self):
        print("parent method called")

class child(parent):
    c = 30
    d = 40

    def childmethod(self):
        print("Child mehtod caleed")

one = child()
print(one.a)
print(one.b)
print(one.c)
print(one.d)
one.parentmethod()
one.childmethod()
