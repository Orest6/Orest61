#Создать класс и вызвать пять объектов этого класса.
class Tools:
    def __init__(self,z):
        self.z = z
    def tools(self):
        print(self.z)

tool1 = Tools('пенал')
tool1.tools()
tool2 = Tools('ручка')
tool2.tools()
tool3 = Tools('карандаш')
tool3.tools()
tool4 = Tools('линейка')
tool4.tools()
tool5 = Tools('точилка')
tool5.tools()
