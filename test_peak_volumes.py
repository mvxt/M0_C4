import random
import unittest

from peak_volumes import get_peak_volumes

class TestGetLoudestSecond(unittest.TestCase):
    def test_basic(self):
        """Tests a basic scenario with random volumes"""
        test = [-34, -27, -32, -62, -71, -45, -12, -53, -16, -44]
        expected = [-34, -27, -27, -27, -27, -27, -12, -12, -12, -12]
        actual = get_peak_volumes(test)
        self.assertEqual(expected, actual)

    def test_all_same(self):
        """Tests a given list with all the same volumes. Output should be the same as input."""
        test = [0] * 20
        actual = get_peak_volumes(test)
        self.assertEqual(test, actual)

    def test_inf_resets_peak(self):
        """Checks that peak is reset after -Inf"""
        test = [-34, -27, -32, -62, -74, -45, -12, -53, -16, -44]
        expected = [-34, -27, -27, -27, '-Inf', -45, -12, -12, -12, -12]
        actual = get_peak_volumes(test)
        self.assertEqual(expected, actual)

    def test_clip_resets_peak(self):
        """Checks that peak is reset after CLIP"""
        test = [-62, -71, -43, 12, -14, -21, -64, -4, -68, -12, -35]
        expected = [-62, -71, -43, 'CLIP', -14, -14, -14, -4, -4, -4, -4]
        actual = get_peak_volumes(test)
        self.assertEqual(expected, actual)

    def test_inf_and_clip(self):
        """Checks multiple CLIPs and -Infs in the song"""
        test = [-62, -71, -43, -343, -14, 0, 521, 43, -68, -12, 5]
        expected = [-62, -62, -43, '-Inf', -14, 0, 'CLIP', 'CLIP', -68, -12, 5]
        actual = get_peak_volumes(test)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
