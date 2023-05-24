def find_max(L,i,m):
    if i:
        m=max(m,L[i-1])
        find_max(L,i-1,m)
        return m

arr=eval(input("Enter an array:"))
if arr==[]:
    print("Empty Array!")
else:
    print("Maximum in array:-")
    print(find_max(arr,len(arr),-float("inf")))
