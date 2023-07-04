import unittest
from application import application


class TestSample(unittest.TestCase):
    def setUp(self):
        application.testing = True
        self.appplication = application.test_client()

    def test_hello(self):
        rv = self.application.get('/')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main()
