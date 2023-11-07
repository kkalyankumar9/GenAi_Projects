import unittest
from app import app


class ZomTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_update_order_status(self):
        response = self.app.patch('/update_order/1', json={"status": "completed"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order 1 status updated to completed', response.data)

    def test_update_order_status_invalid_id(self):
        response = self.app.patch('/update_order/1000', json={"status": "completed"})
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Order with id 1000 not found.', response.data)

    def test_update_order_status_missing_status(self):
        response = self.app.patch('/update_order/1', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input data. Please provide status.', response.data)

    def test_place_order_valid_data(self):
        response = self.app.post('/place_order', json={"customer_name": "John Doe", "dish_ids": [1, 2]})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Order placed successfully with ID', response.data)

    def test_place_order_invalid_dish_id(self):
        response = self.app.post('/place_order', json={"customer_name": "John Doe", "dish_ids": [100, 101]})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Dish with id', response.data)

    def test_place_order_missing_customer_name(self):
        response = self.app.post('/place_order', json={"dish_ids": [1, 2]})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input data. Please provide customer_name and dish_ids.', response.data)

    def test_place_order_missing_dish_ids(self):
        response = self.app.post('/place_order', json={"customer_name": "John Doe"})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input data. Please provide customer_name and dish_ids.', response.data)

if __name__ == '__main__':
    unittest.main()
  
 
