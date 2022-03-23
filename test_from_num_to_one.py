from unittest import main, TestCase
from recusion import from_num_to_one

class Test_from_num_to_one(TestCase):
	# positive tests
	def test_float_number(self):
		print('checking float number')
		self.assertEqual(from_num_to_one(6.1), 1)
		print('float number passed')


	def test_int_number(self):
		print('checking int number')
		self.assertEqual(from_num_to_one(5), 1)
		print('int number passed')


	# negative tests
	def test_string(self):
		print('checking string')
		with self.assertRaises(ValueError) as e:
			from_num_to_one('string')
		print('string pased')

		
if __name__ == '__main__':
	main()