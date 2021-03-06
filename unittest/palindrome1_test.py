import unittest

from palindrome1 import Palindrome

class TestPalindrome(unittest.TestCase):
  def setUp(self):
    self.p1 = Palindrome('abcd')
    self.p2 = Palindrome('abcdedcba')

  def testNormal(self):
    self.assertFalse(self.p1.normal())
    self.assertTrue(self.p2.normal())

unittest.main()
