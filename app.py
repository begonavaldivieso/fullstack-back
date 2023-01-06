from flask import Flask, request, redirect, Response

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print("Nombre recibido por parametro: " + nombre)
    print("Apellidos recibido por parametro: " + apellidos)    
    return redirect("http://localhost//solicita_pedido.html", 302)
    
@app.route("/checksize", methods=['POST'])
def checksize():
    
    size = request.form.get("tamano")
    print(size)
    if size == 'S': 
      mensaje="No disponible"
    else :
      mensaje="Disponible"           
  
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})    