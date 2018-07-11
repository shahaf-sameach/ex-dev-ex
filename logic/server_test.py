from logic import server
import unittest
import json

class ServerTest(unittest.TestCase):

  def setUp(self):
    server.app.testing = True
    self.app = server.app.test_client()

  def test_get_is_blocked(self):
    response = self.app.get('/calculate')
    self.assertTrue(response.status_code == 405)

  def test_calculate_with_valid_data(self):
    response = self.app.post('/calculate',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(dict(input='1',calculatorState="")))
    data = json.loads(response.data)
    self.assertTrue(data['display'] == '1')

  def test_calculate_with_mid_state_number(self):
    response = self.app.post('/calculate',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(dict(input='1',calculatorState=json.dumps({"display": "1"}))))
    data = json.loads(response.data)
    self.assertTrue(data['display'] == '11')

  def test_calculate_with_mid_state_operator(self):
    response = self.app.post('/calculate',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(dict(input='+',calculatorState=json.dumps({"display": "4"}))))
    data = json.loads(response.data)
    self.assertTrue(data['display'] == '4')

  def test_calculate_with_invalid_data(self):
    response = self.app.post('/calculate')
    self.assertTrue(response.status_code == 400)

if __name__ == '__main__':
  unittest.main()