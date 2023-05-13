def countExplodedGems(rows, cols, gems, hits):
    grid = [[0] * cols for _ in range(rows)]
    # Mapping input grid
    for gem in gems:
        i, j, color = gem
        grid[i][j] = color
    res = 0
    for hit in hits:
        hit_row, hit_col = hit
        # Check valid hit position
        if hit_row < 0 or hit_row >= rows or hit_col < 0 or hit_col >= cols or grid[hit_row][hit_col] == 0:
            continue
        
        queue = [(hit_row, hit_col)]
        
        while queue:
            current_row, current_col = queue.pop(0)
            color = grid[current_row][current_col]
            # Check valid position
            if grid[current_row][current_col] == 0:
                continue
            # Explode gem and count it
            grid[current_row][current_col] = 0
            res += 1
            # Continue check surrounding gems
            if current_row > 0 and grid[current_row - 1][current_col] == color:
                queue.append((current_row - 1, current_col))
            if current_row < rows - 1 and grid[current_row + 1][current_col] == color:
                queue.append((current_row + 1, current_col))
            if current_col > 0 and grid[current_row][current_col - 1] == color:
                queue.append((current_row, current_col - 1))
            if current_col < cols - 1 and grid[current_row][current_col + 1] == color:
                queue.append((current_row, current_col + 1))
    return res

rows = 7
cols = 12
gems = [[2, 6, 1],[0, 6, 1],[4, 6, 1],[4, 10, 2],[5, 8, 2],[2, 11, 2],[0, 7, 1],[2, 5, 1],[2, 7, 1],[5, 7, 1],[3, 8, 2],[5, 10, 2],[2, 4, 1],[0, 10, 2],[2, 9, 2],[0, 8, 2],[0, 9, 2],[3, 11, 2],[4, 5, 1],[1, 8, 2],[5, 5, 1],[3, 10, 2],[2, 2, 1],[4, 8, 2],[3, 6, 1],[1, 10, 2],[4, 9, 2],[5, 6, 1],[2, 8, 2],[3, 5, 1],[2, 3, 1],[2, 10, 2],[3, 7, 1],[4, 7, 1],[0, 5, 1]]
hits = [[2, 2], [2, 9], [2,2], [0, 0], [0, 1], [0, 2], [0, 3]]
print(countExplodedGems(rows, cols, gems, hits))