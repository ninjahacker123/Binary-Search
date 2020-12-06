"""
	
	This programme is to demonstrate how binary search is way faster than using a for loop to find an item in a 
	given List / Array, Binary Search is faster with a time complexity of O(log n) ⬅ (in Worst Case Scenario's)  
	wheras time complexity of for loop is O(n) ⬅ (In mostly all Scenario's).

	How a Binary Search works:
		A binary serch begins to work by sorting a list, After doing so it checks if the item in the mddle of the list
		is the target to search for, if so it returns the target, of not it checks if it is greater than or less than 
		the target, and if it is lesser, it selects the portion of list on the right, and vice versa if its greater.
		It proceeds to the while loop (You could also use recursion...) and iterates through the proccess, till the 
		list narrows down to the target.
	
	* Written in the most beginner level I can 😅

	Written in python version 3.8.5

	Author: Joseph Marc Antony  

"""


from binary_search import binary_search as bs

array = [num for num in range(0, 10000)] # Dummy List to Search through
target = 9999 # Target to find in the List ⬆

# Function to Search through List using a For Loop
def loop_search(arr, target):
	count = 0 # Number of iterations made so far using for loop ⬇
	for x in arr:
		if target in arr: # Runs only if target is in the list
			if x == target: # Checks if 'x' is the target
				return f"{target} found at {count} iteration."
				break
			count += 1
		else: # Does not run if target not in list
			return f"For Loop: {target} not in list!"
			break

print(f"For Loop: {loop_search(array, target)}") # Outputs "For Loop: 9999 found at 9999 iteration."
print(f"Binary Search: {bs(array, target)}") # Outputs "Binary Search: 9999 found at 12 iteration."
