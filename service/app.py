import math
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "up"}), 200

@app.route('/sqrt/<value>', methods=['GET'])
def sqrt(value):
    try:
        value = float(value)
    except ValueError:
        return jsonify({"result": None, "error": "Invalid number"}), 400

    if value < 0:
        return jsonify({"result": None, "error": "Negative numbers are not allowed"}), 400
    
    result = math.sqrt(value)
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)