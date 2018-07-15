from __future__ import print_function
from flask import Flask, request
from calculator import Calculator
import os

app = Flask(__name__)

@app.route("/calculate", methods=['POST'])
def calculate():
  if request.is_json:
    try:
      data = request.get_json()
      state = "" if 'calculatorState' not in data.keys() else data['calculatorState']
      response = Calculator.calculateNextState(str(state), str(data['input']))
      return response
    except Exception as e:
      return str(e), 405

  return "bad request", 400
  

if __name__ == "__main__":
  port = int(os.getenv('FLASK_PORT', 5000))
  app.run(host='0.0.0.0', port=port)