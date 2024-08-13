def absolute_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solution(K, A):
    N = len(A)  # 獲取矩陣的行數
    M = len(A[0])  # 獲取矩陣的列數
    
    houses = []
    empty_plots = []
    
    # 遍歷矩陣，找到所有房屋和空地的坐標
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                houses.append((i, j))
            elif A[i][j] == 0:
                empty_plots.append((i, j))
    
    suitable_locations = 0
    
    # 對於每個空地，檢查到每個房屋的距離
    for empty_plot in empty_plots:
        x, y = empty_plot  # 取出空地的坐標
        all_within_distance = True  # 假設該空地符合條件
        
        for house in houses:
            hx, hy = house  # 取出房屋的坐標
            distance = absolute_distance(x, y, hx, hy)  # 計算絕對值距離
            if distance > K:  # 如果距離超過 K，則不符合條件
                all_within_distance = False
                break
        
        if all_within_distance:
            suitable_locations += 1
    
    return suitable_locations

# 示例使用：
K = 2
A = [[0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]
print(solution(K, A))  # 輸出: 2

K = 1
A = [[0, 1], [0, 0]]
print(solution(K, A))  # 輸出: 2

K = 4
A = [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
print(solution(K, A))  # 輸出: 8