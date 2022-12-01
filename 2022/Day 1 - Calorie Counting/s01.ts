const buffer = new Uint8Array(65_536)
const bytesLength = await Deno.stdin.read(buffer) as number
const input = new TextDecoder().decode(buffer.subarray(0, bytesLength))

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
