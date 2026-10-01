#Librerias 
import random # Para generar tareas aleatorias y tiempos estimados
import time # Para simular la ejecución de tareas con un temporizador de cuenta regresiva
import os
import platform

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

class Tarea: # Clase para representar una tarea con un nombre y un tiempo estimado
    def __init__(self, nombre, tiempo_estimado):
        self.nombre = nombre
        self.tiempo_estimado = tiempo_estimado

tarea = Tarea("", 0)
# Lista de tareas posibles
lista = {
    "Tarea de ensamblador de cornejo" , 
    "Tarea de linux de carlos" , 
    "Tarea zzz de claudia" , 
    "Tarea god de meñogod" , 
    "Tarea de redes de sanabria" ,
    "Tarea en equipo del modular" ,
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
# Inicializamos la lista de tareas a partir del conjunto de tareas posibles
lista_de_tareas = list(lista)
tarea_list = []
# Función para generar tareas aleatorias con un tiempo estimado entre 15 y 120 minutos
def generar_tareas():
    nombre = random.choice(lista_de_tareas)
    tiempo_estimado = random.randint(15, 120)
    return Tarea(nombre, tiempo_estimado)

#Algoritmo de SFJ (Shortest Job First) el cual selecciona la tarea con el tiempo estimado más corto de la lista de tareas
def realizar_tarea_mas_corta(tarea_list):
    if not tarea_list:
        raise ValueError("No hay tareas para ejecutar.")
    return min(tarea_list, key=lambda x: x.tiempo_estimado)

#Temporizador de cuenta regresiva
def cuenta_regresiva(tiempo_estimado):
    segundos = round(tiempo_estimado / 15) # 15-120 min -> 1-8 segundos
    while segundos > 0:
        print(f"{segundos} segundos restantes", end="\r")
        time.sleep(1)
        segundos -= 1
    print("\033[92m" + "¡Tarea hecha!        " + "\033[0m")

def ejecutar_tareas():
    print("\033[93m" + "Tareas:" + "\033[0m")
    # Generamos 15 tareas aleatorias y las agregamos a la lista de tareas
    for i in range(15):
        tarea = generar_tareas()
        tarea_list.append(tarea)
        print(f"{i+1}: {tarea.nombre} con tiempo estimado de" + "\033[91m" + f" {tarea.tiempo_estimado}" + "\033[0m" + " minutos")
    # Solicitamos al usuario si desea ejecutar las tareas
    validar = input("\033[94m" + "¿Desea ejecutar las tareas? (s/n): " + "\033[0m")
    # Si el usuario no desea ejecutar las tareas, se cancela la ejecución y se sale del programa
    if validar.lower() != "s":
        print("\033[93m" + "Ejecución de tareas cancelada." + "\033[0m")
        exit()
    # Si el usuario desea ejecutar las tareas, se ejecutan en orden de tiempo más corto (SFJ)
    print ("\033[93m" + "\nEjecutando tareas en orden de tiempo mas corto (SFJ):\n" + "\033[0m")
    for i in range(len(tarea_list)):
        tarea_ejecutar = realizar_tarea_mas_corta(tarea_list)
        print(f"Haciendo: {tarea_ejecutar.nombre} con tiempo de" + "\033[91m" + f" {tarea_ejecutar.tiempo_estimado}" + "\033[0m" + " minutos")
        tarea_list.remove(tarea_ejecutar)
        cuenta_regresiva(tarea_ejecutar.tiempo_estimado)

    print("\033[92m" + "Todas las tareas han sido ejecutadas." + "\033[0m")

def clear(): # Función para limpiar la pantalla de la consola según el sistema operativo (windows)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while True: # Bucle principal del programa que permite ejecutar múltiples rondas de tareas
    clear()  
    ejecutar_tareas()
    # Preguntamos al usuario si desea ejecutar otra ronda de tareas
    validar = input("\033[94m" + "¿Desea ejecutar otra ronda de tareas? (s/n): " + "\033[0m")
    if validar.lower() != "s":
        print("\033[93m" + "Ejecución de tareas finalizada." + "\033[0m")
        break
    else:
        tarea_list.clear()  # Limpiamos la lista de tareas para la siguiente ronda
