def solution():
	reader = open(0)
	drawing = []
	for line in reader:
		if not line.strip():
			break
		drawing.append(line)

	stacks = get_stacks(drawing)
	stacks = perform_procedure(reader, stacks)
	return ''.join(stacks[i].pop() for i in range(len(stacks)))

def get_stacks(drawing: list[str]):
	indices = drawing.pop()
	stack_num = int(indices.rsplit(maxsplit=1)[1])

	stacks = []
	for idx in range(stack_num):
		curr_stack = []
		position = idx * 4 + 1
		for line in reversed(drawing):
			crate = line[position]
			if crate ==  ' ':
				break
			curr_stack.append(crate)
		stacks.append(curr_stack)

	return stacks

def perform_procedure(reader, stacks: list[list[str]]):
	for line in reader:
		move, from_, to = [int(x) for i, x in enumerate(line.split()) if i % 2 == 1]
		for _ in range(move):
			stacks[to - 1].append(stacks[from_ - 1].pop())

	return stacks

print(solution())
