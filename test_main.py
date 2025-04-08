# test_main.py
import unittest
from main import main

class TestTool(unittest.TestCase):
    def test_tool_execution(self):
        # Simulate running the main function
        self.assertTrue(main())

if __name__ == '__main__':
    unittest.main()
