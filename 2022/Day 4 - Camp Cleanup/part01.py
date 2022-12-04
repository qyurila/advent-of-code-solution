def solution():
	counter = 0

	for line in open(0):
		pair = line.split(',')
		elf1, elf2 = map(
			lambda x: list(map(int, x.split('-'))),
			pair
		)

		if (
			elf1[0] >= elf2[0] and elf1[1] <= elf2[1]
		) or (
			elf1[0] <= elf2[0] and elf1[1] >= elf2[1]
		):
			counter += 1

	return counter

print(solution())
