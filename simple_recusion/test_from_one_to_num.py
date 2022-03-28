from unittest import main, TestCase
from recusion import from_one_to_num

class Test_from_one_to_num(TestCase):
	# positive tests
	def test_float_number(self):
		print('checking float number')
		self.assertEqual(from_one_to_num(7.3), None)
		print('float pased')


	def test_int_number(self):
		print('checking int number')
		self.assertEqual(from_one_to_num(8), None)
		print('int pased')


	# negative tests
	def test_string(self):
		print('checking string')
		with self.assertRaises(ValueError) as e:
			self.assertEqual(from_one_to_num('string'), e)
		print('string pased')
if __name__ == '__main__':
	main()