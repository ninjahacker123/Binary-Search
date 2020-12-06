# Binary Search Fucntion ⬇

def binary_search(arr, target):
	arr.sort() # Sorts the List First.
	count = 0 # Iteration Count
	init_num = arr[round(len(arr) / 2) - 1] # Gets the item in the middle

	if init_num == target: # Check if target is already in the middle
		return f"{target} found at {count} iteration."
	elif init_num < target: # if mid num is lesser, slice right portion of the list and assign it to 'search' variable
		search = arr[arr.index(init_num) + 1 : len(arr)]
	elif init_num > target: # if mid num is greater, slice left portion of the list and assign it to 'search' variable
		search = arr[0 : arr.index(init_num)]

	not_found = True

	while not_found: # Repeats the above initial process until found ⬆
		try:	
			num = search[round(len(search) / 2) - 1]
		except IndexError:
			return f"{target} not in list!"
			break
		if num == target:
			return f"{target} found at {count} iteration."
			break
		elif init_num < target:
			search = search[search.index(num) + 1 : len(search)]
		elif num > target:
			search = search[0 : search.index(num)]
		
		count += 1 # Increases Count by 1 after 1 iteration       
