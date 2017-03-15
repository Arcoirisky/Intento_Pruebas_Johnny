def lector(archivo):

	data = open(archivo, "r", encoding="utf-8")
	texto = []
	for linea in data:
		linea = linea.strip().split(',')
		texto.append(linea)
		# print(linea)

	# Primero debo conseguir todas las llaves que se indican en la primera fila
	# menos el id (que es lo primero)
	sub_dicc = {}
	sub_clave_lista = []  # lista con las claves para usarlas despues
	for i in range(1, len(texto[0])):
		palabra = texto[0][i]
		# sub_clave = palabra.rstrip(":string")
		sub_clave = palabra.split(":")[0]
		sub_clave_lista.append([sub_clave, i])
		sub_dicc[sub_clave] = None

	# Despues las asocio a cada id (llave) un diccionario con las otras (recurso,
	# nombre, contraseña, etc)
	dicc = {}
	for linea in texto[1:]:
		dicc_integrado = {}
		for clave, i in sub_clave_lista:
			dicc_integrado[clave] = linea[i]
		# print(dicc_integrado)
		dicc[int(linea[0])] = dicc_integrado
	return dicc
	# print(dicc_integrado)
	# print(dicc)
	# print(dicc.keys())
	# Entonces, dicc es mi diccionario con llave id y como valor el resto de
	# variables

	# Ahora quiero un print que me diga la info de un id

# Esto me lee el archivo de forma bonita. Puede ser utilizado más adelante
# para las opciones avanzadas


def archivo_dice(dicc):

	for elem in dicc.keys():
		texto_entero = ("soy "+str(elem))
		for k, v in dicc[elem].items():
			if v == "":
				v = "ANAF"
			texto_entero += (", mi {} es {} ".format(k, v))
		print(texto_entero)
	# a = dicc["0"].items()
	# print(a)

a = lector("usuarios.csv")
archivo_dice(a)
