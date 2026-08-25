
#operators
#AABCLS (arithmatic, assignment, bitwise, comparision, logical, special) 


#1. Arithmatic op- (+,-,*,/,//,%,**)
a=4
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)#division will give output in float value with decimal point
print(a//b)#floor division will give output in form of decimal value 
print(a%b)#remainder
print(a**b)#power


#task 1
#Get 3 integers input for variables a b c , multiply 3 values, add 3 values,
#then divide the multiplied value by added values and print it.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
R1=a*b*c
R2=a+b+c
print("result is:",R1/R2)


#2. Assignment op - (+=,-=,*=,/=,//=,%=,**=)
x=1
x+=1#x=x+1
print(x)

y=5
y-=4
print(y)

z=4
z*=2
print(z)

#3. Bitwise operator (&, |,^,~,<<,>>)

8421
0000=0
0001=1
0010=2
0011=3
0100=4
0101=5
0110=6
0111=7
1000=8
1001=9
1010=10

#and gate
x y = X*Y
0 0 = 0
0 1 = 0
1 0 = 0
1 1 = 1

#or gate (any one true will get true)
x y = x+y
0 0 = 0
0 1 = 1
1 0 = 1
1 1 = 1

---------


print(4&6)
print(4|6)
print(7&5)
print(8|2)

#XOR gate (same = 0 , diff =1)
print(4^6)
print(7^5)
print(8^2)
print(12^3)


#right shift(>>)
print(2>>1)
print(2>>2)
print(15>>3)
print(13>>3)
print(16>>5)


#left shift(<<)
print(2<<2)
print(11<<4)


#Negation ~ formula : -(n+1)

print(~2)#-2+1=-3


#4. comaprision operator (==, !=, <= , >= , < , > )
x=3
y=8
print(x==y)
print(x!=y)
print(x<=y)
print(x>=y)
print(x<y)
print(x>y)

#5. Logical operators( and , or, not)
x=3
y=8
print(x==y and x!=y)
print(x==y or x!=y)
print(x==y and x!=y or x<=y and x>=y)
print(not(x==y))


#6. special operator
#a.membership : (in, not in)

a=[1,2,3]
print(1 in a)
print(1 not in a)

#b.identity : (is , is not)
a=1
b=2
print(a is b)
print(a is not b)


#important question
what is the difference between == and is ??
== means both value/variable are same or not
is means refering to same memory location 

 







