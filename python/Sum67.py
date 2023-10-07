def sum67(arr):
	six = False
	sum = 0
	
	for num in arr:
		if num == 6:
			six = True
		elif num == 7 and six == True:
			six = False
		elif six == False:
			sum += num
	return sum