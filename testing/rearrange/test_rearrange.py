#!/usr/bin/env python3
import unittest

from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

# Test case for empty value
  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase),expected)

  # Test one name
  def test_one_name(self):
    testcase = "Geiseel"
    expected = "Geiseel"
    self.assertEqual(rearrange_name(testcase),expected)


  # test case for double name
  def test_double_name(self):
    testcase = "Harper, Mooper P."
    expected = "Mooper P. Harper"
    self.assertEqual(rearrange_name(testcase),expected)

# Run the tests
unittest.main()


# from rearrange import rearrange_name
# rearrange_name("Lovelace, Ada")  