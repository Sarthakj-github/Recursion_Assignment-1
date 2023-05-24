def print_arr(arr,i):
    if i:
		print(arr[i-1])
        print_arr(arr,i-1)

arr=eval(input("Enter an array:"))
if arr==[]:
    print("Empty Array!")
else:
    print_arr(arr,len(arr))
