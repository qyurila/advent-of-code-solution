import { readFileSync } from 'fs'
import * as _ from 'lodash/fp'

const input = readFileSync(0, 'utf-8')

const solution = () =>
	_.flow(
		_.split('\n\n'),
		_.map(
			_.flow(
				_.split('\n'),
				_.map(_.toNumber),
				_.sum,
			),
		),
		_.sortBy(_.identity),
		_.takeLast(3),
		_.sum,
	)(input)

console.log(solution())
