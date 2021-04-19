class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        n, m = len(image), len(image[0])
        oldcolor = image[sr][sc]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = []

        def dfs(i, j):
            if image[i][j] == oldcolor:
                image[i][j] = newColor
                visited.append((i, j))
                for di, dj in directions:
                    newi, newj = i + di, j + dj
                    if 0 <= newi < n and 0 <= newj < m and (newi, newj) not in visited:       
                        dfs(newi, newj)
                visited.pop()
        dfs(sr, sc)
        return image