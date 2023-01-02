# Importamos la función persistencia
import persistencia

# Borramos el contenido del fichero pedidos.txt si lo hubiera.
with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

# Declaramos la lista
pedidos = list()
# Rellenamos la lista con los diccionarios
pedidos = [
    {"nombre": "Pedro", "apellidos": "Gil de Diego"},
    {"nombre": "Michael", "apellidos": "Jordan"}
]

# Recorremos la lista y llamos a la funcion persistencia
for pedido in pedidos:
    nombre = pedido["nombre"]
    apellidos = pedido["apellidos"]
    persistencia.guardar_pedido(nombre, apellidos)
