import random

#Integrantes
#Leonel Figueroa Jauregui
#Jose Luis Vidrio Lizaola
#Miguel Angel Ochoa Jacinto
#Ricardo Paredes Sanchez
#Sergio Alexander Coronado Huerta
#Cesar de Jesus Becerra Vera

#SFJ (Shortest job first) Es un algoritmo de planificación de procesos que selecciona el proceso con el 
# tiempo de ejecución más corto para ejecutarse a continuación. Este enfoque puede mejorar la eficiencia 
# del sistema al reducir el tiempo promedio de espera y aumentar la utilización de la CPU.

# Ejemplo de implementación de SFJ en Python: Se asignan tareas con una 
# estimacion de tiempo y se van realizando meediante el algoritmo SFJ.
class Tarea:
    def __init__(self, nombre, tiempo_estimado):
        self.nombre = nombre
        self.tiempo_estimado = tiempo_estimado     

def generar_tareas():
    tiempo = random.randint(15, 120)  

def realizar_tarea_mas_corta(tarea):
