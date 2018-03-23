from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)

@app.route("/calculate", methods=['POST'])
def calculate():
  if request.is_json:
    try:
      data = request.get_json()
      response = Calculator.calculateNextState(data['calculatorState'], data['input'])
      return jsonify(response)
    except:
      pass
            
  return "bad request", 400
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)