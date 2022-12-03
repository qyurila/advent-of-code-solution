import sys

def main():
	curr = 0
	record = 0

	for line in sys.stdin:
		if not line.strip():
			record = max(record, curr)
			curr = 0
			continue

		curr += int(line)

	print(record)

main()
