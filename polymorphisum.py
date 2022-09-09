# methodoverloaddin
class person :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print("")
#         print ( self.name )
#         print ( self.age )
#
#     # def display(self, xyz):
#     #     print ("-----------------",xyz)
#     #     print ( self.name )
#     #     print ( self.age )
#
#     def display(self, *args, **kwargs): # to resolve the method overloading proble
#         print ("-----------------",*args)
#         print ( self.name )
#         print ( self.age )
#
#
# e = person('rup',20)
# e.display('xyz')

#method overriding

class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("")
        print ( self.name )
        print ( self.age )

class stud(person):
    def __init__(self,name,age,studid):
        super().__init__(name,age)
        self.studid = studid
    def display(self):
        super().display()
        print(self.studid)

# e = stud('rup',20,1)
# e.display()


#oprator overloading


class book:
    def __init__(self,name,pages):
        self.name = name
        self.pages =pages

    def display(self):
        print(self.name)
        print(self.pages)

    def __add__(self, other):
        return self.pages +other.pages

b = book('harry potter',1000)
b.display()
b1 = book('mrutunjay',500)
b1.display()
print(b + b1)

