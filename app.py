from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
      <body style="font-family: Arial; padding: 40px;">
        <h1>Backend NFS-e online</h1>
        <p>O sistema está funcionando.</p>
        <p><a href="/status">Ver status</a></p>
      </body>
    </html>
    """

@app.route("/status")
def status():
    return jsonify({
        "ok": True,
        "mensagem": "Backend NFS-e funcionando"
    })

@app.route("/emitir-nfse", methods=["POST"])
def emitir_nfse():
    dados = request.get_json(silent=True) or {}

    return jsonify({
        "ok": True,
        "mensagem": "Recebido com sucesso",
        "xml_recebido": bool(dados.get("xml_nfse")),
        "cnpj_emitente": dados.get("cnpj_emitente", ""),
        "drive_file_id": dados.get("drive_file_id", "")
    })
