import threading

contador = 0
lock1 = threading.Lock()
lock2 = threading.Lock()

def incrementar_con_lock1():
    global contador
    for _ in range(100000):
        with lock1:
            with lock2:
                contador += 1

def incrementar_con_lock2():
    global contador
    for _ in range(100000):
        with lock2:
            with lock1:
                contador += 1

hilo1 = threading.Thread(target=incrementar_con_lock1)
hilo2 = threading.Thread(target=incrementar_con_lock2)

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(contador)

# contador = 0
# lock1 = threading.Lock()
# lock2 = threading.Lock()
#
# def incrementar_ordenado():
#     global contador
#     for _ in range(100000):
#         # Aseguramos que los bloqueos se adquieren en el mismo orden
#         with lock1:
#             with lock2:
#                 contador += 1
#
# hilo1 = threading.Thread(target=incrementar_ordenado)
# hilo2 = threading.Thread(target=incrementar_ordenado)
#
# hilo1.start()
# hilo2.start()
#
# hilo1.join()
# hilo2.join()
#
# print(contador)
