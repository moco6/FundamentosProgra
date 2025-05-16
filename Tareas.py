'''
Clase:        Correlativo de clase
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Nombre del estudiante
Fecha:        2025-05-15
Estado:       [ En progreso | Terminado ]
'''

# Numero Magico

numero = int(input("Introduzca un numero: "))

if numero % 7 == 0 and numero % 5 != 0:
  print("Magico")
else:
  print("Normal")


'''
Clase:        Correlativo de clase
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Nombre del estudiante
Fecha:        2025-05-15
Estado:       [ En progreso | Terminado ]
'''
# Cálculo de impuesto

unidades_consumidas = int(input("Escribe unidades consumidas: "))

if unidades_consumidas > 0 and unidades_consumidas <= 100:
  print ('Sin impuestos')
elif unidades_consumidas > 100 and unidades_consumidas <= 200:
  unidades_consumidas *= 0.5
  print (unidades_consumidas)
elif unidades_consumidas >200:
  unidades_consumidas*= 0.7
  print(f'{unidades_consumidas:.2f}')


'''
Clase:        Correlativo de clase
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Nombre del estudiante
Fecha:        2025-05-15
Estado:       [ En progreso | Terminado ]
'''
# Contra segura

contra = input("Escribe una contra: ")
isdigit = False
isupper = False

for i in contra:
  if i.isdigit():
    isdigit = True
  elif i.isupper:
    isupper = True

if isdigit == True and isupper == True and len(contra) >=8:
  print("Contra segura")
else:
  print("No es segura")


'''
Clase:        Correlativo de clase
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Nombre del estudiante
Fecha:        2025-05-15
Estado:       [ En progreso | Terminado ]
'''
# Automatizando el cálculo de propina

total_cuenta = int(input("Dinero total: "))
propina = int(input("Porcentaje de propina: "))

x = total_cuenta * propina/100

total = total_cuenta + x
print(total)


'''
Clase:        Correlativo de clase
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Definición del ejercicio

Autor:        Nombre del estudiante
Fecha:        2025-05-15
Estado:       [ En progreso | Terminado ]
'''
# División con presición

a = int(input("Escribe un entero: "))

b = int(input("Escribe otro: "))

k = int(input("Cuantos decimales quieres: "))

resultado = a/b

print(f'{resultado:.{k}f}')