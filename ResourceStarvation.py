import threading
import queue
import time

# Creamos una cola para gestionar las solicitudes de impresión
cola_impresion = queue.Queue()

# Función que simula la impresión de un documento
def imprimir_documento(documento):
    print(f"Imprimiendo documento: {documento}")
    time.sleep(1)  # Simulamos el tiempo de impresión
    print(f"Documento {documento} impreso")

# Función que maneja las solicitudes de impresión
def manejar_impresion():
    while True:
        documento = cola_impresion.get()  # Obtenemos un documento de la cola
        imprimir_documento(documento)
        cola_impresion.task_done()  # Marcamos la tarea como completada

# Creamos e iniciamos el hilo encargado de manejar la impresión
hilo_impresion = threading.Thread(target=manejar_impresion)
hilo_impresion.daemon = True  # Establecemos el hilo como daemon para que termine cuando el programa principal termine
hilo_impresion.start()

# Creamos algunos documentos para imprimir
documentos = ["Informe", "Contrato", "Presentacion", "Memo"]

# Agregamos los documentos a la cola de impresión
for documento in documentos:
    cola_impresion.put(documento)

# Esperamos a que todos los documentos sean impresos
cola_impresion.join()

print("Todos los documentos han sido impresos")
