class body:
    def __init__(self,shape,model):
        self.shape = shape
        self.model = model
    def __str__(self):
        return str(self.shape) + '  ' + str(self.model)

b = body("curve","m-12.5")
print(b)


class engine:
    def __init__(self,eng,liter):
        self.eng = eng
        self.liter = liter
    def __str__(self):
        return str(self.eng) +"  "+ str(self.liter)
e = engine("disel","12.5")
print(e)


class tyre:
    def __init__(self,brand,size):
        self.brand = brand
        self.size = size
    def __str__(self):
        return str(self.brand) +  "  " + str(self.size)
t = tyre("avion",45)
print(t)
#encapsulation  has one parent(car) and as many as differnt body to it 
class car:
    def __init__(self,bi,ei,ti):
        self.bi =bi
        self.ei = ei
        self.ti = ti
    def __str__(self):
        return str(self.bi) + "   " +str(self.ei) +"   "+ str(self.ti) + " = always the best model design"
c  = car(b,e,t)
print(c)