import server
import unittest
import json

class FlaskrTestCase(unittest.TestCase):

  def setUp(self):
    server.app.testing = True
    self.app = server.app.test_client()

  def tearDown(self):
    pass

  def test_get_is_blocked(self):
    response = self.app.get('/calculate')
    self.assertTrue(response.status_code == 405)

  # not working...
  def test_calculate_with_valid_data(self):
    response = self.app.post('/calculate', data=dict(
        input='1',
        calculatorState=None
    ))
    data = json.loads(response)
    self.assertTrue(data['display'] == '1')

  def test_calculate_with_invalid_data(self):
    response = self.app.post('/calculate')
    self.assertTrue(response.status_code == 400)

if __name__ == '__main__':
  unittest.main()