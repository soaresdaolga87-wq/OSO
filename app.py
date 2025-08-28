from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pedido")
def pedido():
    dados = {
        "nome": "João Soares",
        "bairro": "Namiteca",
        "latitude": "-15.1167",
        "longitude": "39.2667"
    }
    return render_template("pedido.html", **dados)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
