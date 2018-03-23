import unittest
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

  def setUp(self):
    self.calculateNextState = Calculator.calculateNextState

  def tearDown(self):
    pass

  #TODO: add more tests like this
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


if __name__ == '__main__':
  unittest.main()