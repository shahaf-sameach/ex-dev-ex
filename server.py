from flask import Flask, request, jsonify
from calculator import Calculator
import json

app = Flask(__name__)

@app.route("/calculate", methods=['POST'])
def calculate():
  if request.is_json:
    try:
      data = request.get_json()
      state = None if 'calculatorState' not in data.keys() else data['calculatorState']
      response = Calculator.calculateNextState(state, data['input'])
      return response
    except Exception as e:
      return str(e), 405

  return "bad request", 400
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)