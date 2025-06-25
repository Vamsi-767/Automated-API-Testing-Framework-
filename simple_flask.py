from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"}), 200

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(data), 200

@app.route('/status/<int:code>', methods=['GET'])
def status_code(code):
    return ("", code)
#Hiiii


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

