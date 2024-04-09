file = open('archivo.txt', 'w')
file.write('Este es mi primer archivo\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('Segunda escritura.\n')

file.seek(0)
print(file.read())
file.close()