import turtle
t = turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.speed(30)
col=['yellow', 'green', 'blue', 'white']
c= 0
for i in range(100):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1   
