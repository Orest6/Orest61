#Создайте класс на тему животных.
#В классе должен присутствовать конструктор не менее трёх методов.
class animal:
    def __init__(self,kind,food):
        self.kind = kind
        self.age = 4
        self.food = food
    def a(self):
        print('Вид животного: '+self.kind)
    def gen(self):
        print('Возраст животного: '+str(self.age))
    def ab(self):
        print('Чем питается: '+ self.food)

animal1 = animal('lynx','animals')
animal1.a()
animal1.gen()
animal1.ab()




