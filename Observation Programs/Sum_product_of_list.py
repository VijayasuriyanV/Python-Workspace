
# #l = [1, 5, 6, 3, 5]
l=input("enter the strings by leaving space b/w another numbers:\t").split()
l=list(map(int,l))
print(l)
inp=int(input("\n\nPress number :\n1.Sum\n2.Multiply\n\n\t"))
if(inp==1):
    ans= sum(l)
    print("Sum of all elements in given list: ", ans)
elif(inp==2):
    a = 1
    for i in l:
        a = a * i
    print("Product of all elements in given list: ", a)