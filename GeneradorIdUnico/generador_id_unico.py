# Generador ID Unico
from random import randint

print('*** Sistema de Generador ID Unico ***')
nombre = input('Cual es tu Nombre?: ')
apellido = input('Cual es tu apellido?: ')
anio_nacimiento = input('Cual es tu Año de nacimiento (YYYY)?: ')

nombre_mayuscula = nombre[0:2].upper()
apellido_mayuscula = apellido[0:2].upper()
anio_codigo = anio_nacimiento[2:4]

# Generar un valor de 4 digitos de manera aleatoria
aleatorio = randint(0,9999)

id_unico = f'{nombre_mayuscula}{apellido_mayuscula}{anio_codigo}{aleatorio}'
print(f''' \nHola {nombre}, habitante de la ciudad Gotica! 
    Tu nuevo numero de identificacion (ID) generado por el sistema es:
    {id_unico}
    Felicidades!!!
''')