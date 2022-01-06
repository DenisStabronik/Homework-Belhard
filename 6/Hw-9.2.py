import pickle
class Rectangle :
    '''Это класс Rectangle'''
    # Способ создания объекта 
    def __init__(self, width, height):         
        self.width= width
        self.height = height
    # Метод расчета площади.
    def getArea(self):
        return self.width * self.height
r1 = Rectangle(10,5)

serialized = pickle.dumps(r1)
deserialized = pickle.loads(serialized) 

print(deserialized.getArea())



