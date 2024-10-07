def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

arr = []
n=int(input("Enter the number of values to be inserted  : "))
for i in range(n):
    arr.append(int(input("Enter a value : ")))

target = int(input("Enter the value to be searched : "))
result = linear_search(arr, target)
print(f"Element found at index {result}" if result != -1 else "Element not found")
