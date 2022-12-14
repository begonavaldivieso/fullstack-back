# Funcion que guarda en una fila del fichero pedidos.txt los parametros
def guardar_pedido(nombre, apellidos):
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()
