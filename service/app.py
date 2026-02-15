from flask import Flask, jsonify
from src.square_root import SquareRoot

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "up"}), 200

@app.route('/sqrt/<value>', methods=['GET'])
def sqrt(value):
    try:
        sq = SquareRoot()
        result = sq.run(value)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"result": None, "error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
