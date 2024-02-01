def count_zeros_inside_boundary(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    inside_boundary = False

    # Iteruj po wierszach i kolumnach
    for i in range(rows):
        for j in range(cols):
            # Sprawdź, czy aktualna komórka to granica
            if grid[i][j] == ".":
                inside_boundary = not inside_boundary  # Zmień stan wewnątrz/poza granicą
            elif inside_boundary and grid[i][j] == 0:
                count += 1  # Zlicz zera wewnątrz granicy

    return count

# Przykładowe użycie
grid = [
    [0, 0, 0, ".", ".", ".", ".", "."],
    [0, 0, ".", ".", ".", 0, 0, 0],
    [0, ".", ".", 0, ".", 0, 0, 0],
    [0, ".", ".", ".", ".", 0, 0, 0],
    [0, ".", ".", ".", ".", 0, 0, 0],
    [0, ".", 0, 0, ".", ".", 0, 0],
    [0, ".", 0, 0, 0, ".", 0, 0],
    [0, ".", ".", ".", ".", ".", ".", "."]
]

result = count_zeros_inside_boundary(grid)
print("Ilość zer wewnątrz granicy:", result)
