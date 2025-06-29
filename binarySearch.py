import time

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 1
    while low <= high:
        mid = (low + high) // 2
        print(f"\nStep {steps}:")
        print(f"Low = {low}, High = {high}")
        print(f"Mid Index = {mid}, Mid Value = {arr[mid]}")

        if arr[mid] == target:
            print(f"\n✅ Found {target} at index {mid} in {steps} steps.")
            return mid
        elif arr[mid] < target:
            print(f"{target} > {arr[mid]} → Search Right Half")
            low = mid + 1
        else:
            print(f"{target} < {arr[mid]} → Search Left Half")
            high = mid - 1
        steps += 1
        time.sleep(1)
    print(f"\n❌ {target} not found in the list after {steps - 1} steps.")
    return -1

arr = list(range(1, 101))
print("🔢 Binary Search Demo")
print("List: 1 to 100")
try:
    target = int(input("Enter a Number between 1-100: "))
    binary_search(arr, target)
except ValueError:
    print("Input should be integer")