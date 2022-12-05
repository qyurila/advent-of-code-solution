# IO.read(:stdio, :eof)
File.read!("./input.txt")
|> String.split("\n\n")
|> Enum.map(fn block ->
  block
  |> String.trim()
  |> String.split("\n")
  |> Enum.map(&String.to_integer(&1))
  |> Enum.sum()
end)
|> Enum.sort(:desc)
|> Enum.take(3)
|> Enum.sum()
|> IO.puts()
