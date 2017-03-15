
class Contacto:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Cliente(Contacto):
    def __init__(self, telefono, nombre, email):
        super().__init__(nombre, email)
        self.telefono = telefono


###############

class Contacto:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Patata:

    def __init__(self,verdura):
        self.ver = verdura

class Cliente(Contacto,Patata):
    
    def __init__(self, telefono, nombre, email, verdura):
        Contacto.__init__(self, nombre, email)
        Patata.__init__(self, verdura)
        self.telefono = telefono


b = Cliente("+569","Antonia","pc@cl","patata")
c = b.nombre
d = b.email


#print(c,b.telefono,d,b.ver)

class ClaseB:
    num_llamadas_B = 0
    def llamar(self):
        print("Llamando método en Clase B")
        self.num_llamadas_B += 1

class SubClaseMedia(ClaseB):
    num_llamadas_med = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en Subclase Media")
        self.num_llamadas_med += 1
        
class SubClaseIzquierda(ClaseB):
    num_llamadas_izq = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en Subclase Izquierda")
        self.num_llamadas_izq += 1

class SubClaseDerecha(ClaseB):
    num_llamadas_der = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en Subclase Derecha")
        self.num_llamadas_der += 1

class SubClaseA(SubClaseIzquierda, SubClaseMedia , SubClaseDerecha):
    num_llamadas_subA = 0
    def llamar(self):
        super().llamar()
        print("Llamando método en SubclaseA")
        self.num_llamadas_subA += 1

##s = SubClaseA()
##s.llamar()
##print(s.num_llamadas_subA,s.num_llamadas_med, s.num_llamadas_izq, s.num_llamadas_der, s.num_llamadas_B)

def test(*argv):
    for arg in argv:
        print("siguiente argumento de *argv : {}".format(arg))

t=('hola','como','va','todo')
#test(*t)
#test('hola','como','va')
##test('hola','como')
##test('hola')
##
##
##

def funcion(a=0, b=0):
    return a+b

# Usando solo un valor posicional y el resto usa los argumentos por defecto
valores = (3,)
#print(funcion(*valores))

# Usando todos los argumentos posicionales definidos en la lista
valores = (7,2)
#print(funcion(*valores))

class AddressHolder:
    def __init__(self, calle='', ciudad='', numero='', comuna='',**kwargs):
        super().__init__(**kwargs)
        self.calle = calle
        self.ciudad = ciudad
        self.comuna = comuna
        self.numero = numero


class Contacto:

    contactos_list = []

    def __init__(self, nombre = '', email = '', **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.email = email
        Contacto.contactos_list.append(self)


class Cliente(Contacto, AddressHolder):

    def __init__(self, telefono='', **kwargs):
        super().__init__(**kwargs)
        self.telefono = telefono

c = Cliente(nombre = 'Juan Perez', email = 'jp@gmail.com', telefono = '23542331',
            calle = 'Pedro de Valdivia', numero = '231', comuna = 'Providencia', ciudad = 'Santiago')

print("{}, {}, {}, {}".format(c.nombre, c.email, c.calle, c.comuna))
