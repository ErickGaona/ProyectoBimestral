import threading
import time

# Creamos dos cerrojos
lock1 = threading.Lock()
lock2 = threading.Lock()

# Función para el primer hilo
def tarea1():
    with lock1:
        print("Hilo 1 ha adquirido lock1")
        time.sleep(1)
        with lock2:
            print("Hilo 1 ha adquirido lock2")

# Función para el segundo hilo
def tarea2():
    with lock2:
        print("Hilo 2 ha adquirido lock2")
        time.sleep(1)
        with lock1:
            print("Hilo 2 ha adquirido lock1")

# Creamos e iniciamos los hilos
hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()


# lock1 = threading.Lock()
# lock2 = threading.Lock()
#
# def tarea1():
#     with lock1:
#         print("Hilo 1 ha adquirido lock1")
#         time.sleep(1)
#         with lock2:
#             print("Hilo 1 ha adquirido lock2")
#
# def tarea2():
#     with lock1:  # Cambiamos el orden de adquisición de los cerrojos
#         print("Hilo 2 ha adquirido lock1")
#         time.sleep(1)
#         with lock2:
#             print("Hilo 2 ha adquirido lock2")
#
# hilo1 = threading.Thread(target=tarea1)
# hilo2 = threading.Thread(target=tarea2)
#
# hilo1.start()
# hilo2.start()
#
# hilo1.join()
# hilo2.join()

