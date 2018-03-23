import unittest
from calculator import Calculator

class TestcalculateNextStateMethod(unittest.TestCase):

  def test_calc(self):
    s = Calculator.calculateNextState(None, "1")
    self.assertEqual(s['display'], '1')
    s = Calculator.calculateNextState(s, "2")
    self.assertEqual(s['display'], '12')
    s = Calculator.calculateNextState(s, "+")
    self.assertEqual(s['display'], '12')
    s = Calculator.calculateNextState(s, "4")
    self.assertEqual(s['display'], '4')
    s = Calculator.calculateNextState(s, "3")
    self.assertEqual(s['display'], '43')
    s = Calculator.calculateNextState(s, "=")
    self.assertEqual(s['display'], '55')
    s = Calculator.calculateNextState(s, "+")
    self.assertEqual(s['display'], '55')
    s = Calculator.calculateNextState(s, "1")
    self.assertEqual(s['display'], '1')
    s = Calculator.calculateNextState(s, "=")
    self.assertEqual(s['display'], '56')
    s = Calculator.calculateNextState(s, "5")
    self.assertEqual(s['display'], '5')


if __name__ == '__main__':
  unittest.main()