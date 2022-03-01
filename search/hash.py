# Este tipo de algoritmos es para acomodar millonadas de datos en diferentes lugares para que despues sea mas facil buscar

# m = tamaño de la tabla hash

# Lectura del archivo
f = open('lorem.txt','r')
palabras = [x for l in f.readlines() for x in l.split()]
f.close()
print("cantidad de palabras del texto: {}".format(len(palabras)))

# Aqui se convier
def convertirTextoEnNumero(texto):
	salida = ""

	for x in texto:
		salida += str(ord(x))

	return int(salida)


def hashM(texto, m):
	i = convertirTextoEnNumero(texto)

	return i%m


def agregar(texto, hashTable, m):
	res = hashM(texto, m)
	hashTable[res].append(texto)


def buscar(texto, hashTable, m):
	h = hashM(texto, m)

	for i in hashTable[h]:
		if i == texto:
			return True
	return False


m = 10
hashTable = [[] for i in range(m)]

for palabra in palabras:
	agregar(palabra, hashTable, m)

print("Existe la palabra 'lorem'?: {}".format(buscar("lorem", hashTable, m)))
print("Existe la palabra 'ipsum'?: {}".format(buscar("ipsum", hashTable, m)))
print("Existe la palabra 'pano'?: {}".format(buscar("pano", hashTable, m)))
print("Existe la palabra 'elpanito'?: {}".format(buscar("elpanito", hashTable, m)))