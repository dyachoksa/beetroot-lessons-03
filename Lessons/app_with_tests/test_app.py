import unittest

from app import calculate_tax_amount


class TestCalculateTaxAmount(unittest.TestCase):
    def test_succesfull_calculation(self):
        """should calculate tax amount with default tax percentage in 10%"""
        amount = calculate_tax_amount(1000)
        self.assertEqual(amount, 100, "should be 100")
    
    def test_successfull_calculation_with_5_percent(self):
        """should calculate tax amount with 5% taxation"""
        amount = calculate_tax_amount(1000, tax_percent=5)
        self.assertEqual(amount, 50, "should be 50")
    
    def test_tax_percent_as_none(self):
        """should raise an ValueError if tax percent is None"""
        with self.assertRaises(ValueError, msg="should raise ValueError") as cm:
            calculate_tax_amount(1000, tax_percent=None)
        
        ex = cm.exception
        self.assertEqual(str(ex), "Tax percent can't be None", "should have correct error message")

    def test_tax_percent_is_not_negative(self):
        with self.assertRaises(ValueError) as cm:
            calculate_tax_amount(1000, -10)

        ex = cm.exception
        self.assertEqual(str(ex), "Tax percent can't be negative", "should have correct error message")


if __name__ == "__main__":
    unittest.main()
