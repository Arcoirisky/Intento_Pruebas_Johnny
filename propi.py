class Color:#version con decorador
    
    def __init__(self, rgb_code, nombre):
        self.rgb_code = rgb_code
        self._nombre = nombre
    
    @property 
    def nombre(self):
        print("Obteniendo el nombre del color")
        return self._nombre

    @nombre.setter    
    def nombre(self, valor):
        print("Estas seteando el valor en {}".format(valor))
        self._nombre = valor
        
    @nombre.deleter
    def nombre(self):
        print("Eliminaste el nombre!!")
        del self._nombre     

c = Color("#ff0000", "red")
c.nombre = "azul"
print(c.nombre)
del c.nombre
