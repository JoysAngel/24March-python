import unittest


class TestmyApp2(unittest.TestCase):
    def test_case3(self):
        self.assertEqual("hello", "hello")


class Testmyapp(unittest.TestCase):

    def test_case1(self):
        a = 10
        b = 22
        c = a + b
        self.assertEqual(32, c)

    def test_case2(self):
        self.assertEqual("heljkj", "hello")


if __name__ == "__main__":
    unittest.main()
