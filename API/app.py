from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    # Processamento dos dados recebidos
    return jsonify({"message": "Dados recebidos com sucesso"}), 200

if __name__ == '__main__':
    app.run()