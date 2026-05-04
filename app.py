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

        <hr>
        <h2>Teste de envio</h2>
        <form method="post" action="/emitir-nfse">
          <label>CNPJ do emitente:</label><br>
          <input type="text" name="cnpj_emitente" style="width: 300px;"><br><br>

          <label>Drive File ID:</label><br>
          <input type="text" name="drive_file_id" style="width: 300px;"><br><br>

          <label>XML da NFS-e:</label><br>
          <textarea name="xml_nfse" rows="12" cols="80"></textarea><br><br>

          <button type="submit">Enviar teste</button>
        </form>
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
    if request.form:
        dados = {
            "cnpj_emitente": request.form.get("cnpj_emitente", ""),
            "drive_file_id": request.form.get("drive_file_id", ""),
            "xml_nfse": request.form.get("xml_nfse", "")
        }
    else:
        dados = request.get_json(silent=True) or {}

    return f"""
    <html>
      <body style="font-family: Arial; padding: 40px;">
        <h1>Teste recebido com sucesso</h1>
        <p><b>CNPJ:</b> {dados.get('cnpj_emitente', '')}</p>
        <p><b>Drive File ID:</b> {dados.get('drive_file_id', '')}</p>
        <p><b>XML recebido?</b> {"SIM" if dados.get("xml_nfse") else "NAO"}</p>
        <p><a href="/">Voltar</a></p>
      </body>
    </html>
    """
