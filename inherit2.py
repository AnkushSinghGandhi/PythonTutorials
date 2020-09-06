class calculation1:
    def summation(self,a,b):
        return a+b
class calculation2:
    def multiplication(self,a,b):
        return a*b
class derived(calculation1,calculation2):
    def divide(self,a,b):
        return a/b
d=derived()
print(d.summation(10,20))
print(d.multiplication(10,20))
print(d.divide(10,20))
print(issubclass(derived,calculation1)) #tu check the class is sub class
print(isinstance(d,derived)) #tu check the object belongs to that class