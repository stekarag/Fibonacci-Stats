import unittest
import fibonacci
import fiboFunctions as funcs

class TestFibonacci(unittest.TestCase):

    def test_createFibonacci(self):
        fibo = funcs.createFibonacci(5)
        print(f'fibo gives the array {fibo}')
        nacci = fibonacci.fibonacci(8)
        self.assertEqual(nacci, fibo)
        
    def test_raises_typeError(self):
        self.assertRaises(TypeError, funcs.createFibonacci, "A")

    def test_contains_zero(self):
        self.assertIn(0, funcs.createFibonacci(1))

    def test_lenght(self):
        self.assertTrue(len(funcs.createFibonacci(1)) == 3)

#test = TestFibonacci()
#test.test_createFibonacci()

if __name__ == '__main__':
    unittest.main()