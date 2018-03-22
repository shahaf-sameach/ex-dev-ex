import unittest
from logic import calculateNextState

class TestcalculateNextStateMethod(unittest.TestCase):

  def test_calc(self):
    s = calculateNextState(None, "1")
    self.assertEqual(s['display'], '1')
    s = calculateNextState(s, "2")
    self.assertEqual(s['display'], '12')
    s = calculateNextState(s, "+")
    self.assertEqual(s['display'], '12')
    s = calculateNextState(s, "4")
    self.assertEqual(s['display'], '4')
    s = calculateNextState(s, "3")
    self.assertEqual(s['display'], '43')
    s = calculateNextState(s, "=")
    self.assertEqual(s['display'], '55')
    s = calculateNextState(s, "+")
    self.assertEqual(s['display'], '55')
    s = calculateNextState(s, "1")
    self.assertEqual(s['display'], '1')
    s = calculateNextState(s, "=")
    self.assertEqual(s['display'], '56')


if __name__ == '__main__':
  unittest.main()