import unittest   # The test framework
from my_app.calculations import get_mean, get_std_deviation_pop, get_std_deviation_sample, get_sum

class Test_TestGetMean(unittest.TestCase):
    def test_get_mean(self):
        self.assertEqual(get_mean('test.csv'), 5.619593333333333e-14)

class Test_TestGetStandardDevPop(unittest.TestCase):
    def test_get_std_deviation_pop(self):
        self.assertEqual(get_std_deviation_pop('test.csv'), 6.434052039377846e-14)

class Test_TestGetStandardDevSample(unittest.TestCase):
    def test_get_std_deviation_sample(self):
        self.assertEqual(get_std_deviation_sample('test.csv'), 7.880072237494612e-14)

class Test_TestGetSum(unittest.TestCase):
    def test_get_sum(self):
        self.assertEqual(get_sum('test.csv'), 1.6858779999999998e-13)        

if __name__ == '__main__':
    unittest.main()