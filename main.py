def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the midpoint

        # Check if the target is at the midpoint
        if arr[mid] == target:
            return mid
        # If the target is in the left half
        elif arr[mid] > target:
            right = mid - 1
        # If the target is in the right half
        else:
            left = mid + 1

    # If the target is not in the array
    return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    target = 23

    result = binary_search(arr, target)

    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")
