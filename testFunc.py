import unittest
import func
class testFunc(unittest.TestCase):
    
    def testAdd(self):
        result = func.add(1,1)
        self.assertEqual(result, 2)