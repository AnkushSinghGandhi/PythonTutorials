input("hio")

class employee:
    count=0
    def display(self):
        print("name ",self.name)
        print("id",self.id)
    def __init__(self,name,id):
        self.id=id
        self.name=name
        employee.count=employee.count+1

emp1= employee("ankush",10)
emp2= employee("bhanu",0)
emp3= employee("bhanu",0)
emp1.display()
emp2.display()
emp3.display()
print("no. of employee",employee.count)
