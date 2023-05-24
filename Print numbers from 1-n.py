def print1_n(n):
	if n!=1:
		print1_n(n-1)
	print(n,end=' ')

n=int(input("Enter a number:"))
if n<1:
    print("Invalid Input!")
else:
    print(f"Numbers from 1 to {n} are:-")
    print1_n(n)
