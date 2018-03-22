from flask import Flask, request, jsonify
from logic import calculateNextState

app = Flask(__name__)

@app.route("/calculate", methods=['POST'])
def calculate():
  if request.is_json:
    try:
      data = request.get_json()
      response = calculateNextState(data['calculatorState'], data['input'])
      return jsonify(response)
    except:
      pass

  return "bad request", 400
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)