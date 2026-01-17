from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
usuarios = [
    {"id": 1, "nombre": "Ana", "edad": 25},
    {"id": 2, "nombre": "Carlos", "edad": 30},
    {"id": 3, "nombre": "María", "edad": 28}
]

# Ruta principal
@app.route('/')
def inicio():
    return jsonify({"mensaje": "Bienvenido a mi API", "version": "1.0"})

# Obtener todos los usuarios (GET)
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios, "total": len(usuarios)})

# Obtener un usuario por ID (GET)
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404

# Crear un nuevo usuario (POST)
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    
    if not datos or 'nombre' not in datos or 'edad' not in datos:
        return jsonify({"error": "Datos incompletos"}), 400
    
    nuevo_id = max([u["id"] for u in usuarios]) + 1 if usuarios else 1
    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "edad": datos["edad"]
    }
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

# Actualizar un usuario (PUT)
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    datos = request.get_json()
    if 'nombre' in datos:
        usuario['nombre'] = datos['nombre']
    if 'edad' in datos:
        usuario['edad'] = datos['edad']
    
    return jsonify(usuario)

# Eliminar un usuario (DELETE)
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuario = next((u for u in usuarios if u["id"] == id), None)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    usuarios = [u for u in usuarios if u["id"] != id]
    return jsonify({"mensaje": "Usuario eliminado", "id": id})

if __name__ == '__main__':
    print("🚀 Servidor iniciando en http://127.0.0.1:5000")
    print("\nEndpoints disponibles:")
    print("  GET    /                  - Página de inicio")
    print("  GET    /usuarios          - Listar todos los usuarios")
    print("  GET    /usuarios/<id>     - Obtener usuario por ID")
    print("  POST   /usuarios          - Crear nuevo usuario")
    print("  PUT    /usuarios/<id>     - Actualizar usuario")
    print("  DELETE /usuarios/<id>     - Eliminar usuario")
    app.run(debug=True)
