def print1_n(n):
	print(n,end=' ')
	if n!=1:
		print1_n(n-1)

n=int(input("Enter a number:"))
if n<1:
    print("Invalid Input!")
else:
    print(f"Numbers from {n} to 1 are:-")
    print1_n(n)
