def bubble_sort(a):

    arr = a.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def counting_sort(a):
    if not a:
        return []
    arr = a.copy()
    min_val = min(arr)
    max_val = max(arr)

    range_size = max_val - min_val + 1
    count = [0] * range_size

    for num in arr:
        count[num - min_val] += 1

    result = []
    for i, cnt in enumerate(count):
        value = i + min_val
        result.extend([value] * cnt)

    return result

def bucket_sort(a, buckets: int | None = None):
    if not a:
        return []
    arr = a.copy()
    n = len(arr)
    if buckets is None:
        buckets = n

    bucket_list = [[] for _ in range(buckets)]

    for num in arr:
        index = min(int(num * buckets), buckets - 1)
        bucket_list[index].append(num)

    for i in range(len(bucket_list)):
        bucket_list[i] = insertion_sort(bucket_list[i])

    result = []
    for bucket in bucket_list:
        result.extend(bucket)

    return result

def insertion_sort(bucket):
    arr = bucket.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
