t1= (10,20,30,[40,60,(80,90,'Python')],70)
py = t1[3][2][-1]
print(py[::2])


#list --> mutable
#tuple --> immutable


t1=(10,20,30,40)
#print(t1.append(50))
l1 = list(t1)
l1.append(50)
t1 = tuple(l1)
print(t1)


t1= (10,20,30,[40,60,(80,90)],70)
print(t1[3][2][0])


t1= (10,20,30,[40,60],70)
t1[3].insert(2,90)
print(t1)

#list in tuple mutable
#tuple in list immutableimmutableimmutableimmutableimmutableimmutableimmutableimmutable