#Librerias 
import random
import time

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

tarea = Tarea("", 0)

lista_de_tareas = {
    "Tarea de ensamblador de cornejo" , 
    "Tarea de linux de carlos" , 
    "Tarea zzz de claudia" , 
    "Tarea god de meñogod" , 
    "Tarea de redes de sanabria" ,
    "Tarea en equipo del modular"
    "Exposicion de sergio" ,
    "Investigacion para el modular" , 
    "Guia de estudio para examen de ingles" ,
    "Tarea de metodos numericos" ,
    "Tarea de POO" , 
    "Tarea de ecuaciones diferenciales" ,
    "Tarea de algebra lineal" ,
    "Tarea de circuitos" ,
    "Curso de coursera de bases de datos" , 
    "Curso de redes en Cisco" ,
}

def generar_tareas():
    tarea.tiempo_estimado = random.randint(15, 120)  
    tarea.nombre = random.choice(lista_de_tareas)
    return tarea

#Algoritmo de SFJ
def realizar_tarea_mas_corta(tarea):
    print("xd")


#Funcion de temporizador
def temporizador():
    


    while True:
        for i in range(15):




