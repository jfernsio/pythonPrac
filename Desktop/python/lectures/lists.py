
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7]

print(c)



x = (i for i in range(3))

for i in x: print(i)

for i in x: print(i)

l1=['a','b','c']
l2=['d','e','f']
l3=l1+l2
print(l3)
l3.append("20")
print(l3)


l1=['a','b','c']
l2=['d','e','f']
l1.append("20")
print(l1)
l1.append(l2)
print(l1)



l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)
l1.append("python")
print(l1)
     

l1=[1,2,3]
l2=[4,5,6]
l1.extend(l2)
print(l1)
l1.extend("python")
print(l1)
     

l1=[1,2,3]
l2=[4,5,6]
l1.append(1000)
print(l1)
l1.extend("1000")
print(l1)


l1=[1,2,3,[4,5,6],"python"]
print(l1[3][1])
print(l1[-1][1:])


l1=[1,2,3,[4,5,6,"python"]]
print(l1[3][3][1:])
print(l1[-1][-1][1:])


l1=[1,2,3,[4,5,6,"python"]]
l1[-1].append("programming")
print(l1)


l1=[1,2,3,[30,20,50]]
l1[-1].sort()
print(l1)


l1=['x','y','a','f','h']
l1.sort()
l1.reverse()
print(l1)
l1.insert(2,'w')
print(l1)


l1=[10,20,30,[50,60,[70,80]]]
print(l1[-1][-1][-1])
print(l1[3][2][1])


l1=[10,20,30,[50,60,["python","programming"]]]
print(l1[-1][-1][0],(l1[-1][-1][1]))


import math
l1=[10,20,30,[50,60,[100,200]]]
r1=math.sqrt(l1[-1][-1][0])
r2=math.sqrt(l1[-1][-1][1])
l1.insert([-1][-1][0],r1)
     