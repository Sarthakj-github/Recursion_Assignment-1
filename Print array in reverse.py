def print_rev_arr(arr,i):
    if i:
		print(arr[i-1],end=' ')
		print_rev_arr(arr,i-1)

arr=eval(input("Enter an array:"))
if arr==[]:
	print("Empty Array!")
else:
	print("Printing array in reverse order:-")
    print_rev_arr(arr,len(arr))
