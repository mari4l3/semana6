import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
estudiantes = {}

# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
# Guarda cada par nombre-nota en el diccionario
for i in range(3):
    nombre = input("Ingresa el nombre del estudiante: ")
    nota = float(input(f"Ingresa la nota de {nombre}: "))
    estudiantes[nombre] = nota

# PARTE 2: Calcular promedio
# Usa sum() y len() con el diccionario para calcular el promedio de las notas
promedio = sum(estudiantes.values()) / len(estudiantes)

# PARTE 3: Crear archivo Excel
# Crea un nuevo libro de trabajo
libro = openpyxl.Workbook()

# Obtén la hoja activa
hoja = libro.active

# PARTE 4: Escribir datos
# Escribe "Nombres" en A1, "Notas" en B1 y "Promedio" en C1
hoja['A1'] = "Nombres"
hoja['B1'] = "Notas"
hoja['C1'] = "Promedio"

# Escribe el promedio en C2
hoja['C2'] = promedio

# Usa un ciclo for para escribir los nombres en la columna A y las notas en la columna B
fila = 2  # Comenzamos en la fila 2 para los estudiantes
for nombre, nota in estudiantes.items():
    hoja[f'A{fila}'] = nombre
    hoja[f'B{fila}'] = nota
    fila += 1

# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio5.xlsx"
libro.save("ejercicio5.xlsx")

print("¡Ejercicio 5 guardado en ejercicio5.xlsx!")
