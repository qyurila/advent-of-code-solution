import { readFileSync } from 'fs'
import * as _ from 'lodash/fp'

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
		.sort(
			(a, b) => b - a,
		)
		.slice(0, 3)
		.reduce(
			(prev, curr) => prev + curr,
		)

console.log(solution())
