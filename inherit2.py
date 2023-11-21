class grandparent:
    a = 10
    b = 20

    def grandparentmethod(self):
        print("grandparentmethhod ic called")

class parent(grandparent):

    c = 25
    d = 35

    def parentmethod(self):
        print("parentmethod is called")

class child(parent):

    e = 40
    f = 50

    def childmethod(self):
        print("child method is callled")

one = child()
print(one.a)
print(one.b)
print(one.c)
print(one.d)
print(one.e)
print(one.f)
one.grandparentmethod()
one.parentmethod()
one.childmethod()