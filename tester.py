import unittest
from main import process_orders


class TestProcessOrders(unittest.TestCase):


    def test_product_not_in_inventory(self):
        orders = [{"product": "apple", "quantity": 5}]
        inventory = {"banana": 10}

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)

        self.assertIn("not found in inventory", str(context.exception))


    def test_not_enough_quantity(self):
        orders = [{"product": "apple", "quantity": 100}]
        inventory = {"apple": 10}

        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)

        self.assertIn("Not enough stock", str(context.exception))


    def test_successful_order_updates_inventory(self):
        orders = [{"product": "apple", "quantity": 5}]
        inventory = {"apple": 50}

        result = process_orders(orders, inventory)

        self.assertEqual(result, orders)
        self.assertEqual(inventory["apple"], 45)


if __name__ == "__main__":
    unittest.main()
