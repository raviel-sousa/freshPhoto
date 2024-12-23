from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

# Pegando usuario do banco de dados
@app.route('/usuario', methods=['GET'])
def pegar_usuario():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM usuario")
    usuario = cursor.fetchall()
    return jsonify(usuario), 200

@app.route("/usuario/login", methods=["GET"])
def get_usuario_login():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("CALL login()")
        usuario = cursor.fetchall() 
        return jsonify(usuario), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch products"}), 500

    finally:
        cursor.close()
        conn.close()

@app.route("/usuario/cadastrar", methods=["GET"])
def get_usuario_cadastrar():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("CALL cadastrar()")
        usuario = cursor.fetchall() 
        return jsonify(usuario), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch products"}), 500

    finally:
        cursor.close()
        conn.close()

@app.route("/usuario/perfil", methods=["GET"])
def get_usuario_perfil():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("CALL perfil()")
        usuario = cursor.fetchall() 
        return jsonify(usuario), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch products"}), 500

    finally:
        cursor.close()
        conn.close()

# Criado usuario
@app.route("/usuario/cadastrar", methods=['POST'])
def criar_usuario():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    print(data["img"])
    if "img" in data and data["img"]:
        cursor.execute("""
        INSERT INTO usuario(nome, usuario, senha, email, foto)
        VALUES (%s, %s, %s, %s, %s)
        """, (data["nome"], data["usuario"], data["senha"], data["email"], data["img"]))
    else:
        cursor.execute("""
        INSERT INTO usuario(nome, usuario, senha, email)
        VALUES (%s, %s, %s, %s)
        """, (data["nome"], data["usuario"], data["senha"], data["email"]))
    conn.commit()
    return jsonify({"message": "Usuario criado com sucesso"}), 201

# Criar uma publicação
@app.route("/postagem", methods=["POST"])
def criar_postagem():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO postagem(id_usuario, id_categoria, foto, legenda)
    VALUES (%s, %s, %s, %s)
    """, (data["id_usuario"], data["id_categoria"], data["foto"], data["legenda"]))
    conn.commit()
    return jsonify({"message": "Usuario criado com sucesso"}), 201

if __name__ == '__main__':
    app.run(debug=True)
