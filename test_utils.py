# test_utils.py
from utils import load_config
import unittest

class TestUtils(unittest.TestCase):
    def test_load_config(self):
        config = load_config()
        self.assertIn("host", config)
        self.assertEqual(config["host"], "192.168.1.1")

if __name__ == '__main__':
    unittest.main()
