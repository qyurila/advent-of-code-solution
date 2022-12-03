import sys

def main():
	curr = 0
	sums = []

	for line in sys.stdin:
		# When meet the newline
		if not line.strip():
			sums.append(curr)
			curr = 0
			continue

		curr += int(line)

	print(sum(sorted(sums)[-3:]))

main()
