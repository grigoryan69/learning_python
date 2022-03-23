from unittest import main, TestCase
from recusion import from_num_to_one_short

class Test_from_num_to_one_short(TestCase):
	# positive tests
	def test_float_number(self):
		print('checking float number')
		self.assertEqual(from_num_to_one_short(6.3), 1)
		print('float number passed')


	def test_int_number(self):
		print('checking int number')
		self.assertEqual(from_num_to_one_short(10), 1)
		print('int number passed')


	# negative tests
	def test_string(self):
		print('checking string')
		with self.assertRaises(ValueError) as e:
			from_num_to_one_short('with')
		print('string pased')


if __name__ == '__main__':
	main()