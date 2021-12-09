a=int(input("enter the num_1 value : "))
b=int(input("enter the num_2 value : "))
for i in range(1, min(a,b)+1):
    if((a % i == 0) and (b % i == 0)):
        gcd = i     
print ("The gcd of ",a ,"and " ,b, "is : ",gcd) 
