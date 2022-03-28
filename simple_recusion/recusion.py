#!/usr/bin/env python3
# recursion function to print from 1 to number
def from_one_to_num(num) -> int:
	if int(num) == 0:
		return 0
	else:
		from_one_to_num(int(num) - 1)
	print(int(num))


def main():
	from_one_to_num(100)


if __name__ == '__main__':
	main()
