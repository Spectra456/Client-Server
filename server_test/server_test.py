import unittest
import server.server as server




"""
    All wrong inputs(negative, zero, null, str and other non int) handling by server.
"""
class ServerTest(unittest.TestCase):

    def setUp(self):
        self.server = server.Server()

    def test_prime_factor_1(self):
        self.assertEqual(self.server.prime_Factors(1), 1)

    def test_prime_factor_4(self):
        self.assertEqual(self.server.prime_Factors(4), [2, 2])

    def test_prime_factor_5(self):
        self.assertEqual(self.server.prime_Factors(5), [5])

    def test_prime_factor_10(self):
        self.assertEqual(self.server.prime_Factors(10), [2, 5])

    def test_prime_factor_111111111(self):
        self.assertEqual(self.server.prime_Factors(111111111), [3, 3, 37, 333667])

    def test_prime_factor_001000(self):
        self.assertEqual(self.server.prime_Factors(0o1000), [2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_prime_factor_maxint(self):
        self.assertEqual(self.server.prime_Factors(9223372036854775807), [7, 8, 8, 8, 9, 9, 19, 73, 87211, 262657])



if __name__ == '__main__':
    unittest.main()