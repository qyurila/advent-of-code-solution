def solution():
	buffer = open(0).readline()
	scope_offset = 0
	while True:
		# Search for duplication
		scope = buffer[scope_offset : scope_offset + 4]
		for idx, char in enumerate(scope[:-1]):
			if char in scope[idx + 1 :]:
				# Make while loop continue if there is a duplication
				break
		else:
			# Break while loop if there is no duplication
			break

		scope_offset += 1
		continue

	return scope_offset + 4

print(solution())
