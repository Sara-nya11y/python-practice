arr = list(map(int, input().split()))
arr = list(set(arr))  # duplicates teesey
arr.sort()
print("Second largest:", arr[-2]) if len(arr) >= 2 else print("No second largest")
