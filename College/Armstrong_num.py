# Python program to check if the number is an Armstrong number or not

#armstrong number   Eg: 153 = 1cube +5cube +3cube = 1 +125 + 27 = 153

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit **  3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")