import requests
import unittest
import json

class E2eTestCase(unittest.TestCase):

  def setUp(self):
    self.url = 'http://web:5000/calculate'
    self.headers = {'Content-Type': 'application/json'}

  def test_1(self):
    response = self.__make_request('1', None)
    self.__check_200(response)
    self.__check_display(response.json(), '1')

    response = self.__make_request('2', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '12')

    response = self.__make_request('+', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '12')

    response = self.__make_request('4', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '4')

    response = self.__make_request('3', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '43')

    response = self.__make_request('=', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '55')

    response = self.__make_request('+', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '55')

    response = self.__make_request('1', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '1')

    response = self.__make_request('=', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '56')

    response = self.__make_request('5', response.json())
    self.__check_200(response)
    self.__check_display(response.json(), '5')


  def test_get_is_blocked(self):
    response = requests.get('http://web:5000/calculate')
    self.assertTrue(response.status_code == 405)

  def __check_200(self, response):
    self.assertEqual(response.status_code, 200)

  def __check_display(self, response, display):
    self.assertEqual(response['display'], display)

  def __make_request(self, input_s, state):
    response = requests.post(self.url,
                headers=self.headers,
                data = json.dumps(dict(input=input_s,calculatorState=state)))
    return response



if __name__ == '__main__':
  unittest.main()