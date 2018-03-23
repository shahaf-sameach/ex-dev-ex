import unittest
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

  def setUp(self):
    self.calculateNextState = Calculator.calculateNextState

  def tearDown(self):
    pass

  def test_scenario_1(self):
    s = self.calculateNextState(None, "1")
    self.assertEqual(s['display'], '1')
    s = self.calculateNextState(s, "2")
    self.assertEqual(s['display'], '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(s['display'], '12')
    s = self.calculateNextState(s, "4")
    self.assertEqual(s['display'], '4')
    s = self.calculateNextState(s, "3")
    self.assertEqual(s['display'], '43')
    s = self.calculateNextState(s, "=")
    self.assertEqual(s['display'], '55')
    s = self.calculateNextState(s, "+")
    self.assertEqual(s['display'], '55')
    s = self.calculateNextState(s, "1")
    self.assertEqual(s['display'], '1')
    s = self.calculateNextState(s, "=")
    self.assertEqual(s['display'], '56')
    s = self.calculateNextState(s, "5")
    self.assertEqual(s['display'], '5')

  def test_scenario_2(self):
    s = self.calculateNextState(None, "1")
    self.assertEqual(s['display'], '1')
    s = self.calculateNextState(s, "2")
    self.assertEqual(s['display'], '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(s['display'], '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(s['display'], '12')
    s = self.calculateNextState(s, "+")
    self.assertEqual(s['display'], '12')
    s = self.calculateNextState(s, "3")
    self.assertEqual(s['display'], '3')
    s = self.calculateNextState(s, "4")
    self.assertEqual(s['display'], '34')
    s = self.calculateNextState(s, "=")
    self.assertEqual(s['display'], '46')

  def test_start_in_mid_state_with_number(self):
    s = {"display": "1"}
    s = self.calculateNextState(s, "1")
    self.assertEqual(s['display'], "11")
  
  def test_start_in_mid_state_with_operator(self):
    s = {"display": "4"}
    s = self.calculateNextState(s, "+")
    self.assertEqual(s['display'], "4")


if __name__ == '__main__':
  unittest.main()