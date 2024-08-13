import math

def solution(S):
    # 用 '\n' 拆分每條記錄
    call_logs = S.split('\n')
    
    # 用於存儲每個電話號碼的總時長和總費用的字典
    total_durations = {}
    call_costs = {}
    
    for log in call_logs:
        # 忽略空行
        if not log.strip():
            continue
        
        # 拆分時長和電話號碼
        duration, phone_number = log.split(',')
        
        # 將 hh:mm:ss 轉換為總秒數
        hh, mm, ss = map(int, duration.split(':'))
        total_seconds = hh * 3600 + mm * 60 + ss
        
        # 計算通話的費用
        if total_seconds < 300:
            cost = total_seconds * 3  # 每秒 3 分
        else:
            # 計算總分鐘數（無條件進位）
            total_minutes = math.ceil(total_seconds / 60)
            cost = total_minutes * 150  # 每分鐘 150 分
        
        # 更新電話號碼的總時長和費用
        if phone_number in total_durations:
            total_durations[phone_number] += total_seconds
            call_costs[phone_number] += cost
        else:
            total_durations[phone_number] = total_seconds
            call_costs[phone_number] = cost
    
    # 找出總通話時長最長的電話號碼
    max_duration = -1
    longest_duration_phone_number = None
    
    for phone_number, duration in total_durations.items():
        if duration > max_duration:
            max_duration = duration
            longest_duration_phone_number = phone_number
        elif duration == max_duration:
            # 如果有相同時長，選擇數值最小的電話號碼
            if phone_number < longest_duration_phone_number:
                longest_duration_phone_number = phone_number
    
    # 計算排除最長時長電話號碼後的總費用
    total_cost = 0
    for phone_number, cost in call_costs.items():
        if phone_number != longest_duration_phone_number:
            total_cost += cost
    
    return total_cost

# 測試函數，使用給定的範例
S = "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090"
print(solution(S))  # 輸出應為 900