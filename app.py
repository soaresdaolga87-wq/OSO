from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 API/Servidor Flask ativo no Render! Vá para /pedido ou /dashboard"

@app.route("/pedido")
def pedido():
    return render_template("pedido.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
