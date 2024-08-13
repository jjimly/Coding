def solution(N):
    d = [0] * 30
    l = 0
    while (N > 0):
        d[l] = N % 2
        N //= 2
        l += 1

    # 原始代碼：
    # for p in range(1, 1 + l):
    for p in range(1, l // 2 + 1):  # 修正1: 僅檢查P <= Q/2的情況
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1

# 測試案例
print(solution(955))  # 預期輸出：4
print(solution(10))   # 預期輸出：2
print(solution(1))    # 預期輸出：-1 (因為1的二進制是"1"，無周期)
print(solution(6))    # 預期輸出：-1 (因為6的二進制是"110"，無周期)
print(solution(12))   # 預期輸出：2 (因為12的二進制是"1100"，周期是2)
