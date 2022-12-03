from string import ascii_letters


def solution():
	priority_map = '_' + ascii_letters
	result = 0

	for line in open(0):
		line = line.strip()
		half = len(line) // 2
		first_half, second_half = map(set, (line[:half], line[half:]))

		dup = first_half & second_half
		result += priority_map.find(*dup)

	return result

print(solution())
