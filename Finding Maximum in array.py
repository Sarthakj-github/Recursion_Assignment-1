def find_max(L,i):
	if i:
		return max(-float('inf'),find_max(L,i-1))
	return -flaot('inf')
arr=eval(input("Enter an array:"))
if arr==[]:
	print("Empty Array!")
else:
	print("Finding maximum in array:-")
    print_arr(arr,len(arr))
