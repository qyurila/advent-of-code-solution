point_map = %{
  "A" => 0,
  "B" => 1,
  "C" => 2,
  "X" => 0,
  "Y" => 1,
  "Z" => 2
}

File.read!("./input.txt")
|> String.trim()
|> String.split("\n")
|> Enum.map(fn line ->
  [oppo, result] =
    line
    |> String.split()
    |> Enum.map(&point_map[&1])

  Integer.mod(oppo + result - 1, 3) + 1 + result * 3
end)
|> Enum.sum()
|> IO.puts()
