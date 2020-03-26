import random
import unittest

from loudest_second import get_loudest_second

class TestGetLoudestSecond(unittest.TestCase):
    def test_loudest_basic(self):
        test = [-34, -27, -32, -62, -71, -45, -12, -53, -16, -44]
        output = get_loudest_second(test)
        self.assertEqual(6, output)

    def test_loudest_all_same(self):
        test = [0] * 20
        output = get_loudest_second(test)
        self.assertEqual(0, output)

    def test_loudest_multiple_same(self):
        test = [-34, -27, -32, -62, -12, -45, -12, -53, -16, -44]
        output = get_loudest_second(test)
        self.assertEqual(4, output)

    def test_loudest_invalid_minimum(self):
        test = [-62, -71, -43, -153, -14, -21, -64, -72, -68, -12, -35]
        output = get_loudest_second(test)
        self.assertEqual("Invalid", output)

    def test_loudest_invalid_maximum(self):
        test = [-62, -71, -43, -71, -14, 0, -64, 43, -68, -12, 5]
        output = get_loudest_second(test)
        self.assertEqual("Invalid", output)

    def test_loudest_outrageous_size(self):
        test = []
        for x in range(36234):
            test.append(random.randint(-72,9))
        index = random.randint(0, 36235)
        test[index] = 10
        output = get_loudest_second(test)
        self.assertEqual(index, output)

if __name__ == '__main__':
    unittest.main()
