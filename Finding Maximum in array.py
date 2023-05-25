def find_max(L,i):
    if i:
        return max(L[i],find_max(L,i-1))
    return L[i]

arr=eval(input("Enter an array:"))
if arr==[]:
    print("Empty Array!")
else:
    print("Maximum in array:-")
    print(find_max(arr,len(arr)-1))
