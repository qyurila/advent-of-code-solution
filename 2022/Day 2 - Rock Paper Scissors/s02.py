import sys

def solution():
	score = 0

	for line in sys.stdin:
		oppo, outcome_char = map(lambda x: x.strip(), line.split(' '))

		oppo_shape, outcome = map(
			lambda x, y: x.find(y),
			['ABC', 'XYZ'], [oppo, outcome_char]
		)

		score += (oppo_shape + outcome - 1) % 3 + 1
		score += outcome * 3
		print(oppo_shape, outcome, score)

	print(score)

solution()
