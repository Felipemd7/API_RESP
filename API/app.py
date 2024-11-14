from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    
    # Verifica se o JSON contém os campos obrigatórios
    required_fields = ["device_id", "temperature", "humidity", "luminosity", "rssi", "pdr"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo '{field}' ausente no JSON"}), 400
    
    # Extrai e organiza os dados
    try:
        device_id = str(data["device_id"])
        temperature = float(data["temperature"])  # Convertendo para float
        humidity = float(data["humidity"])        # Convertendo para float
        luminosity = float(data["luminosity"])    # Convertendo para float
        rssi = int(data["rssi"])                  # Convertendo para int
        pdr = float(data["pdr"])                  # Convertendo para float
    except ValueError as e:
        return jsonify({"error": f"Erro de tipo de dado: {str(e)}"}), 400
    
    # Estrutura organizada dos dados recebidos
    organized_data = {
        "device_id": device_id,
        "temperature": temperature,
        "humidity": humidity,
        "luminosity": luminosity,
        "rssi": rssi,
        "pdr": pdr
    }
    
    # Exemplo de retorno com os dados organizados (opcional, ou apenas salva no banco de dados)
    return jsonify({"message": "Dados recebidos com sucesso", "data": organized_data}), 200

if __name__ == '__main__':
    app.run(debug=True)
