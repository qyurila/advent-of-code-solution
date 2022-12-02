import { readFileSync } from 'fs'
const input = readFileSync(0, 'utf-8')

const solution = () =>
	input
		.split('\n\n')
		.map(block =>
			block
				.split('\n')
				.map(line => Number(line))
				.reduce((prev, curr) => prev + curr)
		)
		.reduce(
			(prev, curr) => prev > curr ? prev : curr,
		)

console.log(solution())
