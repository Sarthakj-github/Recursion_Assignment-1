def print_arr(arr,i,n):
    if i<n:
        print(arr[i],end=' ')
        print_arr(arr,i+1,n)

arr=eval(input("Enter an array:"))
if arr==[]:
    print("Empty Array!")
else:
    print_arr(arr,0,len(arr))
