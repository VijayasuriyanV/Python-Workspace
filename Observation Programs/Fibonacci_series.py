n=int(input('Enter a value for n :'))

a=c=0
b=i=1
print('fibbonacci series')
while i <= n:
    print(a)
    c = a + b
    a ,b= b,c
    i += 1
