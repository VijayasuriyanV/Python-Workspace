#Area of circle 
def area_of_circle():
    r=float(input("Enter the radius value: "))
    print("Area of circle is = %.2f" %(3.14*r**2))

#--------------------------------------------------------------------------
#Area of triangle 
def area_of_triangle():
    b=float(input("Enter the breadth value: "))
    h=float(input("Enter the height value: "))
    area=0.5*b*h
    print("Area of Triangle is = %.2f" %area)

#Celsius_to_fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))

#--------------------------------------------------------------------------

#GCD
def gcd():
    a=int(input("enter the num_1 value : "))
    b=int(input("enter the num_2 value : "))
    for i in range(1, min(a,b)+1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
    print ("The gcd of ",a ,"and " ,b, "is : ",gcd)

#--------------------------------------------------------------------------

#Greater_among_3

def greater_among_3():
    a=int(input("Enter the value_1 : "))  # if u want to input decimal value then use float data_type
    b=int(input("Enter the value_2 : "))
    c=int(input("Enter the value_3 : "))
    print("The greatest number among 3 is : ", max(a,b,c))

#--------------------------------------------------------------------------

#Hello_world
def hello_world():
    print("Hello world! \U0001F609")

#--------------------------------------------------------------------------

#Leap_year
def leap_year():
    year=int(input("Enter the year : "))
    if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        print(year," is Leap year " )
    else:
        print(year," is not a Leap year")   
 
 #--------------------------------------------------------------------------
 
 #Multiplication_table
def multiplication_table():
    num = int(input("Display multiplication table of? "))
    for i in range(1, 11):
        print(num, 'x', i, '=', num*i)

#----------------------------------------------------------------------------


#Number_positive_or_neg

def positive_or_negative():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

#--------------------------------------------------------------------------

#Sum of the two numbers

def sum_of_two_numbers():
    a=int(input("Enter the value_1 to add:"))
    b=int(input("Enter the value_2 to add:"))
    print(a+b)

#--------------------------------------------------------------------------


#Swap the two numbers

def swap_two_numbers():
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    a,b = b,a
    print("The value of a is ",a)
    print("The value of b is ",b)

#--------------------------------------------------------------------------


#circulate_n_variables
def circulate_n_variables():
    n = int(input("Enter number of values to store in list: "))
    l = []
    
    for val in range(0,n,1):
        num= int(input("Enter the integer : "))
        l.append(num)
    print("Circulating the elements of list ", l)
    
    for val in range(0,n,1):
        num = l.pop(0)
        l.append(num)
        print(l)


#--------------------------------------------------------------------------

#Distance_between_points

def distance_between_points():
    import math
    x1 = int(input("Enter coordinates for Point 1 : \n x1 = "))
    y1 = int(input("Enter coordinates for Point 1 : \n y1 = "))

    x2 = int(input("Enter coordinates for Point 2 : \n x2 = "))
    y2 = int(input("Enter coordinates for Point 2 : \n y2 = "))
    
    dist = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

    print("Distance between given points is", round(dist,2))

#--------------------------------------------------------------------------


#All in program 
print("\n\nH4I , H4VE 4 NICE D4Y\n\n")
print("Choose Any one Program\n")
print(" 1.Area of Circle\n 2.Area of Triangle\n 3.Celsius to Fahrenheit\n 4.GCD\n 5.Greater number among the 3 numbers\n 6.Print Hello World\n 7.Multiplication Table\n 8.To check the number is positive or Not\n 9.Sum of two numbers\n 10.Swap two numbers\n 11.To check Leap year\n 12.To Circulate N variables\n 13.To Find Distance between points\n\n")
prog=int(input("Enter the number , of which program you want to use : "))
print("\n\n")
if(prog==1):
    print("Area of Circle ........................")
    area_of_circle()
  
elif(prog==2):
    print("Area of Triangle ........................")
    area_of_triangle()
   
elif(prog==3):
    print("Celsius To Fahrenheit ........................")
    celsius_to_fahrenheit()
   
elif(prog==4):
    print("  GCD ........................")
    gcd()
  
elif(prog==5):
    print("Greater number Among 3 numbers ........................")
    greater_among_3()
 
elif(prog==6):
    print("Hello World ........................")
    hello_world()   
   
elif(prog==7):
    print("Multiplication Tables ........................")
    multiplication_table()

elif(prog==8):
    print("To check the number is positive or Negative ........................")
    positive_or_negative()
  
elif(prog==9):
    print("Sum of two Numbers ........................")
    sum_of_two_numbers()
  
elif(prog==10):
    print("Swapping to variables ........................")
    swap_two_numbers()
    
elif(prog==11):
    print("To check leap year or not ........................")
    leap_year()
elif(prog==12):
    print("To Circulate N Variables ........................")
    circulate_n_variables()
elif(prog==13):
    print("To Find Distance between points ........................")
    distance_between_points()
else:
    print("Invalid Option")

print("\nThe End of the Program")    


