import time
from sorters import counting_sort, radix_sort
from utils import generate_data, verify_sorted

def run_experiment():
    N = 1000000
    print(f"--- 實驗開始：排序 {N} 個 16-bit 整數 ---")
    
    # 產生數據
    data = generate_data(N)
    
    # 1. 內建 sorted()
    start = time.perf_counter()
    res_builtin = sorted(data)
    t_builtin = time.perf_counter() - start
    print(f"【Built-in sorted】: {t_builtin:.4f} 秒")

    # 2. Counting Sort
    start = time.perf_counter()
    res_counting = counting_sort(data)
    t_counting = time.perf_counter() - start
    print(f"【Counting Sort 】: {t_counting:.4f} 秒")

    # 3. Radix Sort
    start = time.perf_counter()
    res_radix = radix_sort(data)
    t_radix = time.perf_counter() - start
    print(f"【Radix Sort    】: {t_radix:.4f} 秒")

    # 驗證
    is_correct = (res_builtin == res_counting == res_radix)
    print(f"\n所有演算法結果一致: {is_correct}")

if __name__ == "__main__":
    run_experiment()
