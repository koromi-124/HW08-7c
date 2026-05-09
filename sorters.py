# sorters.py

def counting_sort(arr):
    """
    計數排序：適用於 16-bit 整數 (0-65535)
    時間複雜度: O(N + K), K = 65536
    """
    if not arr:
        return arr
    
    # 建立 65536 個桶子
    max_val = 65535
    counts = [0] * (max_val + 1)
    
    # 統計頻率
    for x in arr:
        counts[x] += 1
    
    # 重建陣列：使用 Python 的 extend 優化速度
    sorted_arr = []
    for val, count in enumerate(counts):
        if count > 0:
            sorted_arr.extend([val] * count)
    return sorted_arr

def radix_sort(arr):
    """
    基數排序：使用 Base 256 (Byte-wise)
    針對 16-bit，只需進行 2 輪排序
    時間複雜度: O(d * (N + K)), d=2, K=256
    """
    if not arr:
        return arr

    current_arr = arr
    # 進行兩輪，第一輪處理低 8 位 (bits 0-7)，第二輪處理高 8 位 (bits 8-15)
    for p in range(2):
        buckets = [[] for _ in range(256)]
        shift = p * 8
        for x in current_arr:
            # 取得當前 Byte 的數值作為桶子索引
            digit = (x >> shift) & 0xFF
            buckets[digit].append(x)
        
        # 攤平桶子 (Flatten)
        current_arr = [item for bucket in buckets for item in bucket]
            
    return current_arr
