from string import ascii_letters

def solution():
	rl = open(0).readline
	priority_map = '_' + ascii_letters
	result = 0

	while True:
		group = [set(rl().strip()) for _ in range(3)]
		if not group[0]:
			break

		dup = group[0] & group[1] & group[2]
		result += priority_map.find(*dup)

	return result

print(solution())
