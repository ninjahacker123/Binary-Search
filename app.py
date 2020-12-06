from binary_search import binary_search as bs

array = [num for num in range(0, 10000)]
target = 9999


def loop_search(arr, target):
	count = 0
	for x in arr:
		if target in arr:
			if x == target:
				return f"{target} found at {count} iteration."
				break
			count += 1
		else:
			return f"For Loop: {target} not in list!"
			break

print(f"For Loop: {loop_search(array, target)}") # Outputs "For Loop: 9999 found at 9999 iteration."
print(f"Binary Search: {bs(array, target)}") # Outputs "Binary Search: 9999 found at 12 iteration."
