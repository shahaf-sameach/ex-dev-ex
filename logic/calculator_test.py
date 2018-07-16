import unittest
import json
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

  def setUp(self):
    self.calculateNextState = Calculator.calculateNextState

  def tearDown(self):
    pass

  def test_scenario_1(self):
    s = self.calculateNextState(None, "1")
    self.assertEqual(self.__get_display(s), '1')
    s = self.calculateNextState(s, "2")
    self.assertEqual(self.__get_display(s), '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(self.__get_display(s), '12')
    s = self.calculateNextState(s, "4")
    self.assertEqual(self.__get_display(s), '4')
    s = self.calculateNextState(s, "3")
    self.assertEqual(self.__get_display(s), '43')
    s = self.calculateNextState(s, "=")
    self.assertEqual(self.__get_display(s), '55')
    s = self.calculateNextState(s, "+")
    self.assertEqual(self.__get_display(s), '55')
    s = self.calculateNextState(s, "1")
    self.assertEqual(self.__get_display(s), '1')
    s = self.calculateNextState(s, "=")
    self.assertEqual(self.__get_display(s), '56')
    s = self.calculateNextState(s, "5")
    self.assertEqual(self.__get_display(s), '5')

  def test_scenario_2(self):
    s = self.calculateNextState(None, "1")
    self.assertEqual(self.__get_display(s), '1')
    s = self.calculateNextState(s, "2")
    self.assertEqual(self.__get_display(s), '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(self.__get_display(s), '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(self.__get_display(s), '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(self.__get_display(s), '12')
    s = self.calculateNextState(s, "3")
    self.assertEqual(self.__get_display(s), '3')
    s = self.calculateNextState(s, "4")
    self.assertEqual(self.__get_display(s), '34')
    s = self.calculateNextState(s, "=")
    self.assertEqual(self.__get_display(s), '46')

  def test_start_in_mid_state_with_number(self):
    s = {"display": "1"}
    s = self.calculateNextState(json.dumps(s), "1")
    self.assertEqual(self.__get_display(s), "11")
  
  def test_start_in_mid_state_with_operator(self):
    s = {"display": "4"}
    s = self.calculateNextState(json.dumps(s), "+")
    self.assertEqual(self.__get_display(s), "4")

  def test_subtraction(self):
    s = self.calculateNextState(None, "1")
    self.assertEqual(self.__get_display(s), '1')
    s = self.calculateNextState(s, "8")
    self.assertEqual(self.__get_display(s), '18')
    s = self.calculateNextState(s, "-")
    self.assertEqual(self.__get_display(s), '18')
    s = self.calculateNextState(s, "1")
    self.assertEqual(self.__get_display(s), '1')
    s = self.calculateNextState(s, "0")
    self.assertEqual(self.__get_display(s), '10')
    s = self.calculateNextState(s, "=")
    self.assertEqual(self.__get_display(s), '8')

  def test_multiplication(self):
    s = self.calculateNextState(None, "1")
    self.assertEqual(self.__get_display(s), '1')
    s = self.calculateNextState(s, "1")
    self.assertEqual(self.__get_display(s), '11')
    s = self.calculateNextState(s, "*")
    self.assertEqual(self.__get_display(s), '11')
    s = self.calculateNextState(s, "5")
    self.assertEqual(self.__get_display(s), '5')
    s = self.calculateNextState(s, "=")
    self.assertEqual(self.__get_display(s), '55')

  def test_division(self):
    s = self.calculateNextState(None, "4")
    self.assertEqual(self.__get_display(s), '4')
    s = self.calculateNextState(s, "5")
    self.assertEqual(self.__get_display(s), '45')
    s = self.calculateNextState(s, "/")
    self.assertEqual(self.__get_display(s), '45')
    s = self.calculateNextState(s, "9")
    self.assertEqual(self.__get_display(s), '9')
    s = self.calculateNextState(s, "=")
    self.assertEqual(self.__get_display(s), '5')

  def __get_display(self, state):
    return json.loads(state)['display']


if __name__ == '__main__':
  unittest.main()