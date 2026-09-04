#python identity operator exercise
#a =[1, 2, 3, 4]
#b = a
#print("a is b:", a is b)

a= [1, 2, 3, 4]
b= [1, 2, 3, 4]
print("a is b:", a is b)
c=[1,3,4,7,]
d=[1,3,4,7]
result=d is c # is identity operator
print("result of",d,"is",result,"c is",c)
e=[1,2,3,4,5,6,7,]
f=[1,2,3,6,7,8,9,0]
result=f and e # and operator
print("result of",f,"and",e,"and operator is',result")
g=[1,2,3,4,5,6,7,]
h=[1,2,3,6,7,8,9,0]
result=h and g # is not  operator
print("result of",h,"is not",g,"is not operator is',result")
