from collections import deque

def bfs_distance(grid, start):
    N, M = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    distances = [[float('inf')] * M for _ in range(N)]
    queue = deque([start])
    distances[start[0]][start[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and distances[nx][ny] == float('inf'):
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    
    return distances

def solution(K, A):
    N, M = len(A), len(A[0])
    houses = [(i, j) for i in range(N) for j in range(M) if A[i][j] == 1]
    empty_plots = [(i, j) for i in range(N) for j in range(M) if A[i][j] == 0]
    
    if not houses or not empty_plots:
        return 0
    
    # Compute distance from each house to all cells
    distance_from_houses = [bfs_distance(A, house) for house in houses]
    
    suitable_locations = 0
    
    for x, y in empty_plots:
        if all(distance_from_houses[house_idx][x][y] <= K for house_idx in range(len(houses))):
            suitable_locations += 1
    
    return suitable_locations

# Example usage:
K = 2
A = [[0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]
print(solution(K, A))  # Output: 2

K = 1
A = [[0, 1], [0, 0]]
print(solution(K, A))  # Output: 2

K = 4
A = [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
print(solution(K, A))  # Output: 8