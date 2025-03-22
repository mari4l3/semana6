Programa Python: Nombres y Promedios a Excel:

Este programa en Python solicita al usuario los nombres y notas de tres estudiantes, 
guarda esta información en un diccionario y luego escribe los nombres y promedios de las notas en un archivo Excel.


1.  **Crear un entorno virtual:**

    * Crear un entorno virtual para aíslar las dependencias del proyecto de las del sistema.
    Para crear un entorno virtual, se abre una terminal y se ejecuta:

        python3 -m venv venv

    Esto creará un directorio llamado `venv` que contiene el entorno virtual.

2.  **Activar el entorno virtual:**

    * En macOS y Linux:
      
        source venv/bin/activate

    * En Windows:

        venv\Scripts\activate

3.  **Instalar las dependencias:**

    * Con el entorno virtual activado, se instalan las dependencias incluidas en el archivo requirements.txt, para
      esto, se usara el comando:
      
        pip install -r requirements.txt

## Uso:

1.  **Ejecutar el programa:**

    * El codigo de programa se encuentra en el archivo main.py
    * Ejecuta el programa desde la terminal:

        
        python main.py
      

2.  **Ingresar datos:**

    * El programa te pedirá que ingreses el nombre y las notas de cada estudiante.
    * Sigue las instrucciones en la terminal.

3.  **Resultado:**

    * El programa creará un archivo Excel llamado `Ejercicio5.xlsx` en el proyecto.
    * El archivo Excel contendrá los nombres de los estudiantes en la columna A, las notas en la columna B
      y el promedio de sus notas en la columna C.
