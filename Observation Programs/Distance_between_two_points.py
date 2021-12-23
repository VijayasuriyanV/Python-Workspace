import math
x1 = int(input("Enter coordinates for Point 1 : \n x1 = "))
y1 = int(input("Enter coordinates for Point 1 : \n y1 = "))

x2 = int(input("Enter coordinates for Point 2 : \n x2 = "))
y2 = int(input("Enter coordinates for Point 2 : \n y2 = "))
    
dist = math.sqrt( ((x2-x1)**2) + ((y2-y1)**2) )

print("Distance between given points is", round(dist,2))