from flask import Flask, request, jsonify, render_template
import xmlrpc.client

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/previsao", methods=["POST"])
def previsao_tempo():
    data = request.get_json()
    cidade = data["cidade"]
    servidor = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)
    previsao = servidor.obter_previsao(cidade)
    return jsonify(previsao)

if __name__ == "__main__":
    app.run(debug=True)
