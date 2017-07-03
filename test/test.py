import unittest
import sys
sys.path.append('../src')
import core

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(core.absolute(10), 10)

if __name__ == '__main__':
    unittest.main()

### test code goes here
