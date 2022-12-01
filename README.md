# QriLa's Advent of Code playground

## Env

- Python: 3.11.0

## Tips

- Python
  - Use `sys.stdin` (over `input()`)
    - Read one line: `sys.stdin.readline()`
    - Iterate lines: `for line in sys.stdin`
      - or `for line in open(0)`

- TypeScript
  - Deno offers their own stdin (and stdout) API: `Deno.stdin.read`

```ts
const buffer = new Uint8Array(65_536)
const bytesLength = await Deno.stdin.read(buffer) as number
const input = new TextDecoder().decode(buffer.subarray(0, bytesLength))
```
