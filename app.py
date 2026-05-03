from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
      <head>
        <title>Teste Python</title>
      </head>
      <body style="font-family: Arial; padding: 40px;">
        <h1>Servidor Python funcionando</h1>
        <p>Se você está vendo isso, o Flask está rodando certo.</p>
        <p><a href="/status">Ver status</a></p>
      </body>
    </html>
    """

@app.route("/status")
def status():
    return jsonify({
        "ok": True,
        "mensagem": "Python funcionando com sucesso"
    })
