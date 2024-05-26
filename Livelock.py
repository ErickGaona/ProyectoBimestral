import threading

puerta = threading.Lock()

def persona1():
    while True:
        puerta.acquire()
        print("Persona 1 intenta pasar.")
        puerta.release()

def persona2():
    while True:
        puerta.acquire()
        print("Persona 2 intenta pasar.")
        puerta.release()

thread_persona1 = threading.Thread(target=persona1)
thread_persona2 = threading.Thread(target=persona2)

thread_persona1.start()
thread_persona2.start()

thread_persona1.join()
thread_persona2.join()
