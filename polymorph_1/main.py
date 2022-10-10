class Car:
    def __init__(self,name_model = 'Tesla',marka = 'x',colour = 'grey'):
        self.name_model = name_model
        self.marka = marka
        self.colour = colour
    def Info(self):
        print('Марка машины: ' + self.name_model +',', ' название модели: ' + self.marka, ',',' цвет машины: ' + self.colour)
class BMW(Car):
    def __init__(self,colour = 'acid yellow'):
        self.colour = colour
    def Info(self):
        print('Цвет машины: ' + self.colour)
car1 = Car('audi','x','black')
car1.Info()
bmw1 = BMW('black')
bmw1.Info()
car2 = Car()
car2.Info()
bmw2 = BMW()
bmw2.Info()