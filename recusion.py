#!/usr/bin/env python3
# recursion function to print from number to 1
def from_num_to_one(num) -> int:
	print(int(num))
	if int(num) == 1:
		return 1
	else:
		return from_num_to_one(int(num) - 1)


# same recursion function to print from number to 1 but shorter
def from_num_to_one_short(num) -> int:
	print(int(num))
	return 1 if int(num) == 1 else from_num_to_one_short(int(num) - 1)


# recursion function to print from 1 to number
def from_one_to_num(num) -> int:
	if int(num) == 0:
		return 0
	else:
		from_one_to_num(int(num) - 1)
	print(int(num))


def main():
	from_num_to_one(100)
	from_num_to_one_short(100)
	from_one_to_num(100)


if __name__ == '__main__':
	main()


