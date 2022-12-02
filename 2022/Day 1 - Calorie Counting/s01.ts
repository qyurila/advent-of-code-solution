import { readFileSync } from 'fs'
import * as _ from 'lodash/fp'

const input = readFileSync(0, 'utf-8')

const solution1 = () =>
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

const solution2 = () =>
	_.flow(
		_.split('\n\n'),
		_.map(
			_.flow([
				_.split('\n'),
				_.map(_.toNumber),
				_.sum,
			]),
		),
		_.max,
	)(input)

console.log(solution2())
