import time
from typing import Callable, Dict, List, Any

def timeit_once(func: Callable, *args, **kwargs) -> float:
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time

def benchmark_sorts(arrays: Dict[str, List], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    results = {}
    for algo_name, algo_func in algos.items():
        results[algo_name] = {}
        for array_name, array in arrays.items():
            array_copy = array.copy()
            try:
                exec_time = timeit_once(algo_func, array_copy)
                results[algo_name][array_name] = exec_time
            except Exception as e:
                results[algo_name][array_name] = float('inf')
    return results
