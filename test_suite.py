from sorters import counting_sort, radix_sort

def verify_and_report(name, original, result):
    """通用驗證函式"""
    expected = sorted(original)
    if result == expected:
        print(f"✅ {name:15} | 測試通過")
        return True
    else:
        print(f"❌ {name:15} | 結果錯誤！")
        # 顯示前 10 個不符合的地方
        diff = [(i, e, r) for i, (e, r) in enumerate(zip(expected, result)) if e != r]
        print(f"   前幾處錯誤 (索引, 預期, 實際): {diff[:3]}")
        return False

def run_tests():
    print("--- 開始演算法正確性測試 ---")
    
    # 案例 A：小規模隨機資料
    small_data = [5, 3, 8, 1, 9, 3, 2, 10]
    verify_and_report("Small Random", small_data, counting_sort(small_data))
    verify_and_report("Small Random", small_data, radix_sort(small_data))

    # 案例 B：邊界值測試 (16-bit 範圍)
    edge_data = [0, 65535, 32768, 0, 1, 65534]
    verify_and_report("Edge Cases", edge_data, counting_sort(edge_data))
    verify_and_report("Edge Cases", edge_data, radix_sort(edge_data))

    # 案例 C：全部相同或已排序
    same_data = [100] * 10
    verify_and_report("All Same", same_data, counting_sort(same_data))
    
    # 案例 D：10萬筆大規模隨機比對 (黃金標準)
    import random
    large_data = [random.randint(0, 65535) for _ in range(100000)]
    verify_and_report("100K Random", large_data, counting_sort(large_data))
    verify_and_report("100K Random", large_data, radix_sort(large_data))

if __name__ == "__main__":
    run_tests()
