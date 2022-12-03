import sys

def solution():
	score = 0

	for line in sys.stdin:
		oppo, me = map(lambda x: x.strip(), line.split(' '))

		oppo_shape_score, my_shape_score = map(
			lambda x, y: x.find(y),
			['_ABC', '_XYZ'], [oppo, me]
		)
		score += my_shape_score
		score += (my_shape_score - oppo_shape_score + 1) % 3 * 3

	print(score)

solution()
