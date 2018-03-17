import unittest
from business import Business
class businessTestCase(unittest.TestCase):
	def test_create_business(self):
		business = Business()
		response = business.create_business("naibor","lolo")
		self.assertEqual(response["message"],"business added successfully")

	def test_cannot_create_duplicate_business(self):
		pass