import unittest
from stack import Stack

class TestStackMethods(unittest.TestCase):

    # def __init__(self,obj:Stack()):
    #     self.obj = obj
    def test_append(self,value):
        self.obj.append(value)
        self.assertEqual(value,self.obj.peek())

    def test_obj(self):
        pass
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()