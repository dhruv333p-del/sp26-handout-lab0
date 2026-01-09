"""Tests for Lab 0 Question 1"""

import sys
sys.path.append(".")
import unittest
from src.q1 import is_palindrome
assert is_palindrome("racecar") == True
assert is_palindrome("level") == True
assert is_palindrome("kayak") == True
assert is_palindrome("Moonlight") == False