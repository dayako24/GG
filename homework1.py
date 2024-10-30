#1

#a=float(input("a"))
#print(4*a)

#2

#a=float(input("a"))
#print(a**2)

#3

#a=float(input())
#b=float(input())
#print(2*a+2*b)
#print(a*b)

#4

#d=float(input())
#p=3.14
#print(d*p)

#5

#a=float(input())
#print(a**3)
#print(6*a**2)

#6

#a=float(input())
#b=float(input())
#c=float(input())
#print(a*b+b*c+c*a)
#print(a*b*c)

#7

#r=float(input())
#p=3.14
#print(p*r**2)
#print(2*p*r)

#8

#a=float(input())
#b=float(input())
#print((a+b)/2)
#9
a=float(input())
b=float(input())
print((a*b)**0.5)
#10
a=float(input())
b=float(input())
print(a+b)
print(a*b)
print(a**2)
print(b**2)
#11
a=float(input())
b=float(input())
print(a*b)
print(a+b)
print((a**2)**0.5)
print((b**2)**0.5)
#12
a=float(input())
b=float(input())
c=(a**2+b**2)**0.5
print((a**2+b**2)**0.5)
print(a+b+c)
#13
a=float(input())
b=float(input())
p=3.14
x=p*a**2
y=p*b**2
z=x-y
print(x)
print(y)
print(z)
#14
a=float(input())
p=3.14
r=a/(2*p)
s=p*r**2
print(r)
print(s)
#15
a=float(input())
p=3.14
r=(s/p)**0.5
print(r)
print(2*r)
#16
a=float(input())
b=float(input())
s=a-b
print((s**2)**0.5)
#17
a=float(input())
b=float(input())
c=float(input())
AC=c-a
BC=c-b
print(AC)
print(BC)
print(AC+BC)
#18
a=float(input())
b=float(input())
c=float(input())
AC=c-a
BC=b-c
print(AC*BC)
#19
a=float(input())
b=float(input())
c=float(input())
d=float(input())
x=abs(a-c)
y=abs(b-d)
print(x*y)
print(2*(x+y))
#21
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
x=((a-c)**2+(b-d)**2)**0.5
y=((e-c)**2+(f-d)**2)**0.5
x=((a-e)**2+(b-f)**2)**0.5
p=(x+y+z)/2
print((p*(p-x)*(p-y)*(p-z))**0.5
print(x+y+z)
#20
a=float(input())
b=float(input())
c=float(input())
d=float(input())
x=((a-c)**2+(b-d)**2)**0.5
print(x)
#22
a=float(input())
b=float(input())
x=a+b 
a=x-a
b=x-b
print(a)
print(b)
#23
a=float(input())
b=float(input())
c=float(input())
a, b, c= b, c, a 
print(a)
print(b)
print(c)
#24
a=float(input())
b=float(input())
c=float(input())
a, b, c= c, a, b 
print(a)
print(b)
print(c)
#25
x=float(input())
y=3*x**6-6*x**2-7
print(y)
#26
x=float(input())
y=4*(x-3)**6-7*(x-3)*3+2
print(y)
#27
A=float(input())
print(A**2)
print(A**5)
print(A**9)
#29
a=float(input())
print(a/360*p)
#30
a=float(input())
p=3.14
print(a/p*360)
#33
a=float(input())
b=float(input())
print(a*b)
#34
a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(abs(a/b-c/d))
#35
a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(c*(a+b)+d*(a-b))
#36
a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(c+a*d+b*d)
#37
a=float(input())
b=float(input())
c=float(input())
d=float(input())
print(c-(a+b)*d)
#38
a=float(input())
b=float(input())
print(0-b/a)
#39
a=float(input())
b=float(input())
c=float(input())
d=b**2-4*a*c
if d>=0:
    x1=(-b-d**0.5)/(2*a)
    x2=(-b+d**0.5)/(2*a)
    print(x1,' ', x2)
else:
    print("tenglama yechimga ega emas") 
#40
B1 = float(input())
C1 = float(input())
A1 = float(input())
A2 = float(input())
B2 = float(input())
C2 = float(input())   
D = A1 * B2 - A2 * B1
if D != 0:
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    print(x," ",y)
else:
    print("sistema yechimga ega emas")

