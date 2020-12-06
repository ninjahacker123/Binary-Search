def binary_search(arr, target):
	arr.sort()
	count = 0 
	init_num = arr[round(len(arr) / 2) - 1]

	if init_num == target:
		return f"{target} found at {count} iteration."
	elif init_num < target:
		search = arr[arr.index(init_num) + 1 : len(arr)]
	elif init_num > target:
		search = arr[0 : arr.index(init_num)]

	not_found = True

	while not_found:
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
		
		count += 1        
