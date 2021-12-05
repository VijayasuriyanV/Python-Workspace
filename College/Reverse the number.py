#Reverse the number


num = (input("Enter a number: ")) #int data type not support in slicing , it  assumes as string
rev_num=num[::-1]
print(rev_num)

#ANOTHER METHOD

#num = 1234
#reversed_num = 0

#while num != 0:
#    digit = num % 10
 #   reversed_num = reversed_num * 10 + digit
 #   num //= 10

#print("Reversed Number: " + str(reversed_num))