

#creating new list from existing list
lis=[1,2,3,4,5,6,7,8,9,10]
value_to_remove = [3,5,6,7]
new=[]
for i in lis:
    if i not in value_to_remove:
        new.append(i)
print(new)


IN BUILT FUNCTIONS
#insert(), 
#syntax -- var.insert(index,val)

#remove()
syntax-- list.remove(val)

#pop()
syntax-- 1. empty pop will remove last value
        2. with argument it will remove index valued item

l=[1,1,3,4,]
l.insert(1,2)
l.remove(1)
l.pop(2)
print(max(l))
print(min(l))
pritn(len(l))
print(l)
        


#minimun number in list without using inbuilt function
list=[1,2,3,4,5,6,7,8]
min= 1
for i in list:
    if i < min:
        min= i
print(min)


#max
list=[1,2,3,4,5,6,7,8]
max= 0
for i in list:
    if i > max:
        max= i
print(max)



#List comprehension -- concise
#syntax -- new=[exp for var in seq if condition]


#1.list square using comprehension--
lst=[1,2,3,4]
new=[i**2 for i in lst]
print(new)


#2.list even number using comprehension --
lst=[1,2,3,4,5,6]
new=[i for i in lst if i%2==0]
print(new)


#3.new list from existing list using comprehension
lis=[10,20,30,45,59,60]
v=[20,59]
new=[i for i in lis if i not in v]
print(new)


#4.sum of n numbers program by taking user input into list and then sum the list
x = int(input("Enter a number: "))
y = [i for i in range(x+1)]
print(sum(y))












