import threading
import time

def preparar_cafe():
    print("Barista A está preparando el café...")
    time.sleep(2)  # Simulando el tiempo de preparación
    print("Barista A ha terminado el café!")

def preparar_te():
    print("Barista B está preparando el té...")
    time.sleep(3)  # Simulando el tiempo de preparación
    print("Barista B ha terminado el té!")

def preparar_chocolate():
    print("Barista C está preparando el chocolate caliente...")
    time.sleep(4)  # Simulando el tiempo de preparación
    print("Barista C ha terminado el chocolate caliente!")

# Creación de hilos para cada tarea
hilo_cafe = threading.Thread(target=preparar_cafe)
hilo_te = threading.Thread(target=preparar_te)
hilo_chocolate = threading.Thread(target=preparar_chocolate)

# Iniciar hilos
hilo_cafe.start()
hilo_te.start()
hilo_chocolate.start()

# Esperar a que todos los hilos terminen
hilo_cafe.join()
hilo_te.join()
hilo_chocolate.join()

print("Todas las bebidas han sido preparadas!")
