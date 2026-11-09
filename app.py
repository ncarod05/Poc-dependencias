from flask import Flask
from importlib.metadata import version  # Nativa de Pythonapp = Flask(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    # Obtener la versión de Flask instalada (prueba de que requirements.txt funciona)
    flask_version = version("flask")
    
    return f"""
    <h1>¡Bienvenido a la aplicación de demostración de CI/CD!</h1>
    <p>Pipeline actualizado y desplegado correctamente en Kali Linux.</p>
    <p><strong>Dependencia activa:</strong> Flask versión {flask_version}</p>
    """

if __name__ == "__main__":
    # Escucha en todas las interfaces en el puerto 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
