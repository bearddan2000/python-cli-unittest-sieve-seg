from io import StringIO
from unittest.mock import patch
import unittest

import main

class TestMain(unittest.TestCase):
    """docstring for TestMain."""
    def test_simpleSieve(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.simpleSieve(5)
            self.assertEqual(captured.getvalue(), "2 3 ")

    def test_segmentedSieve(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.segmentedSieve(5)
            self.assertEqual(captured.getvalue(), "2 3 ")
