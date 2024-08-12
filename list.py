thislist = ["cherry","banana","apple"]
print(thislist)

thislist = ["cherry","banana","apple","cherry","apple"]
print(thislist)

thislist=["cherry","banana","grapes"]
print(len(thislist))

list1 = ["apple","orange","cherry"]
list2 = [1,5,9,4]
list3 = [True,False,False]
print(list1)
print(list2)
print(list3)

list1=["abc",23,True,55,"male"]
print(list1)

mylist=["apple","banana","cherry"]
print(type(mylist))

  #acesslist

school=list(["students","teachers","principal"])
print(school)

fruits=["apple","banana","grapes"]
print(fruits[2])

student=["ram","sislly","rosyy"]
print(student[-2])

school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
print(school[2:4])

school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
print(school)

school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
print(school[:4])

school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
print(school[2:])

school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
print(school[-4:-1])

radio=["audience","stage","car"]
if "stage" in radio:
    print("yes,'apple' is in the fruits list")

#changeitem

road= ["peoples","vehicles","building"]
road[2]="malls"
print(road)

fruits=["Peach","Pear","Plum","Cherry","Pomegranate","Apricot","Fig","Dragonfruit","Guava","Lychee","Passion Fruit","jackfruit"]
fruits[1:3]=["apple","pineapple"]
print(fruits)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add list items

road=["men","women","children"]
road.append("cycle")
print(road)

hostel=["room","bed","toilet"]
hostel.insert(1,"space")
print(hostel)

men=["perfume","makeup","shampoo"]
soap=["santoor","lux","chandrika"]
men.extend(soap)
print(men)

#remove list items

gym=["zoomba","dance","exercise"]
gym.remove("dance")
print(gym)

home=["father","mother","son","daughter"]
home.pop(2)
print(home)


rose=["farm","grass","water"]
del rose[0]
print(rose)

juice=["water","juicepowder","apple"]
juice.clear()
print(juice)

#loop lists

balaruma=["story","book","malyalam"]
for x in balaruma:
    print(x)


door=["room","bench","chair"]
for i in range(len(door)):
    print(door[i])

jorge=["house","plan","area"]
i=0
while i<len(jorge):
    print(jorge[i])
    i=i+1

makeup=["material","usage","skin","bride","men"]
i=2
while i<len(makeup):
    print(makeup[i])
    i=i+1


ganamo = ["music","instruments","artists"]
[print(x)for x in ganamo]

naptol=["juicer","cars","steels"]
[print(x)for x in naptol]

fruits=["apple","banana","cherry","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if"a" in x:
        newlist.append(x)
print(newlist)

road=["men","women","children","vehicles","tarring"]
newlist=[x for x in road if "e" in x]
print(newlist)


fruits=["apple","banana","cherry","cherry","kiwi","mango"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)

newlist=[x for x in range(10)]
print(newlist)

song=[x for x in range(20)]
print(song)


newlist=[x for x in range(10)if x<5]
print(newlist)


makeup=["material","usage","skin","bride","men"]
newlist=[x.upper()for x in makeup]
print(newlist)


balaruma=["story","book","malyalam"]
newlist=['hello' for x in balaruma]
print(newlist)

school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
newlist=[x if x!= "teacher" else "manali" for  x in school]
print(newlist)


#sortlist


fruits=["Peach","Pear","Plum","Cherry","Pomegranate","Apricot","Fig","Dragonfruit","Guava","Lychee","Passion Fruit","jackfruit"]
fruits.sort()
print(fruits)

cumdoo =[1,2,3,44,55,7,9]
cumdoo.sort()
print(cumdoo)

fruits=["apple","banana","cherry","cherry","kiwi","mango"]
fruits.sort(reverse=True)
print(fruits)


dj=[1,8,4,0,2,5]
dj.sort(reverse=True)
print(dj)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

def myfunc(n):
    return abs(n-50)
thislist=[100,50,45,80,20]
thislist.sort(key=myfunc)
print(thislist)


thislist=["banana","orange","kiwi","cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

gangster=["men","women","rascals","gang"]
gangster.reverse()
print(gangster)


#copylist

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["jam", "butterfly", "rose"]
mylist = list(thislist)
print(mylist)


thislist = ["jamews", "bishop", "urekka"]
mylist = thislist[:]
print(mylist)

#join list


list1=["a","b","c","d"]
list2=[1,2,3,4]
list3=list1+list2
print(list3)

list1=["a","b","c","d"]
list2=[1,2,3,4]
for x in list2:
    list1.append(x)
print(list1)
