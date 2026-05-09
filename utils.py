import random

def generate_data(n=1000000):
    """產生 n 個 16-bit 隨機整數 (0-65535)"""
    return [random.randint(0, 65535) for _ in range(n)]

def verify_sorted(original, result):
    """驗證結果是否正確排序"""
    return result == sorted(original)
