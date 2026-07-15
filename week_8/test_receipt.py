import contextlib
import io
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from receipt import print_receipt


class ReceiptTests(unittest.TestCase):
    def test_receipt_calculates_grand_total(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            total = print_receipt("Izzad", "Cake", 2, 3.00, "Y")

        self.assertAlmostEqual(total, 11.30, places=2)
        self.assertIn("Grand Total : RM 11.30", output.getvalue())


if __name__ == "__main__":
    unittest.main()
