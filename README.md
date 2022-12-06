# QriLa's Advent of Code playground

## Env

- Python: 3.11.0
- TypeScript: 4.9.3
  - Node.js: 18.12.1

## Cheatsheet

- Python
  - Use `sys.stdin` (over `input()`)
    - Read one line: `sys.stdin.readline()`
    - Iterate lines: `for line in sys.stdin`
      - or `for line in open(0)`

- TypeScript
  - ~~Deno offers their own stdin (and stdout) API: `Deno.stdin.read`~~
  - Node offers two method for stdin.

<details>
<summary>Example Snippets</summary>

```ts
// Deno
const buffer = new Uint8Array(65_536)
const bytesLength = await Deno.stdin.read(buffer) as number
const input = new TextDecoder().decode(buffer.subarray(0, bytesLength))

// Node
// - readFileSync
import { readFileSync } from 'fs'
const input = readFileSync(0, 'utf-8')

// - readline
import { stdin } from 'node:process'
import * as readline from 'node:readline'

const rl = readline.createInterface({ input: stdin })

rl.on('line', (line) => {
  // Handle line
})
// or
for await (const line of rl) {
  // Handle line
}
```

</details>

- Elixir
  - `IO.read(:stdio, :eof)` does not work for some reason. It just stuck after getting EOF.
    - Walkaround: use `File.read!("./input.txt")` instead.
  - `rem/2` is different to `Integer.mod/2` and can return a negative.
