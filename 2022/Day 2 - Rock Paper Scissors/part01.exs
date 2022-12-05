point_map = %{
  "A" => 1,
  "B" => 2,
  "C" => 3,
  "X" => 1,
  "Y" => 2,
  "Z" => 3
}

File.read!("./input.txt")
|> String.trim()
|> String.split("\n")
|> Enum.map(fn line ->
  [oppo, mine] =
    line
    |> String.split()
    |> Enum.map(&point_map[&1])

  # rem/2 is different to Integer.mod/2 and can return a negative!
  mine + Integer.mod(mine - oppo + 1, 3) * 3
end)
|> Enum.sum()
|> IO.puts()
