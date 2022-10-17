class x :
    pass
class a(x):
    pass
    # def display(self):
    #     print("display of a")
class b(x):
    pass
    # def display(self):
    #     print("display of b")
class c(x):
    pass
    # def display(self):
    #     print("display of c")
class d(a,b):
     pass
    # def display(self):
    #     print("display of d")
class e(b,c):
    # pass
        def display(self):
            print("display of e")
class f(d,e):
    pass
    # def display(self):
    #     print("display of f")

f1 =f()
f1.display()
print(f.mro())

