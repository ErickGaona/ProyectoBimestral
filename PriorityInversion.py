import threading
import time

# Creamos un cerrojo para simular un recurso compartido
cerrojo = threading.Lock()

# Función que simula el acceso al recurso compartido por el hilo de baja prioridad
def hilo_baja_prioridad():
    with cerrojo:
        print("Hilo de baja prioridad (C) accediendo al recurso compartido...")
        time.sleep(2)  # Simulamos un trabajo en el recurso compartido
        print("Hilo de baja prioridad (C) ha terminado de acceder al recurso compartido")

# Función que simula el acceso al recurso compartido por el hilo de alta prioridad
def hilo_alta_prioridad():
    print("Hilo de alta prioridad (A) necesita acceder al recurso compartido")
    with cerrojo:
        print("Hilo de alta prioridad (A) accediendo al recurso compartido...")
        time.sleep(1)  # Simulamos un trabajo en el recurso compartido
        print("Hilo de alta prioridad (A) ha terminado de acceder al recurso compartido")

# Creamos los hilos con diferentes prioridades
hilo_a = threading.Thread(target=hilo_alta_prioridad)
hilo_b = threading.Thread(target=hilo_baja_prioridad)

# Asignamos prioridades
hilo_a.start()
hilo_b.start()

hilo_a.join()
hilo_b.join()

print("Todos los hilos han terminado")
