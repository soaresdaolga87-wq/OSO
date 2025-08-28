from flask import Flask, render_template

app = Flask(__name__)

@app.route("/pedido")
def pedido():
    # Aqui simulamos os dados que virão do usuário ou banco
    dados = {
        "nome": "João Soares",
        "bairro": "Namiteca",
        "latitude": "-15.1167",
        "longitude": "39.2667"
    }
    return render_template("pedido.html", **dados)

if __name__ == "__main__":
    app.run(debug=True)
