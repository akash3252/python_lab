def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
nterms=int(input("enter the no of terms:"))
if nterms<=0:
    print("enter a positive no")
else:
    print("fibonacci series")
    for i in range (nterms):
        print(fibo(i))