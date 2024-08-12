#sets

forman={"harry","gopikaa","orman","rakav"}
print(forman)


filmfestivals={"actors","directors","musicals","anchors","actors","musicals","anchors"}
print(filmfestivals)

#set() constructor

ganster=set(("gamer","jorgert","konik","jermy"))
print(ganster)


#access items

gamer={"play","win","fail"}
for x in gamer:
    print(x)

#add set items

makeup={"material","usage","skin","bride","men"}
makeup.add("facial")
print(makeup)


#add set

home={"father","mother","son","daughter"}
rose={"farm","grass","water"}
home.update(rose)
print(home)


gamer={"play","win","fail"}
x=gamer.pop()
print(x)
print(gamer)


#loop sets

rose={"flower","beauty","smell"}
for x in rose:
    print(x)

# join set

sremen = {"a","b","r"}
grany = {1,2,3}
farmen = sremen.union(grany)
print(farmen)

sremen = {"a","b","r"}
grany = {1,2,3}
farmen = sremen | grany
print(farmen)


door={"room","bench","chair"}
ganamo = {"music","instruments","artists"}
school={"teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"}
road={"men","women","children"}
Dragon =door.union(ganamo,school,road)
print(Dragon)

door={"room","bench","chair"}
ganamo = {"music","instruments","artists"}
school={"teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"}
road={"men","women","children"}
Dragon =door| ganamo| school| road
print(Dragon)


grammer={"a","b","c","d"}
berm=(1,2,3,4)
gross=grammer.union(berm)
print(gross)

#intersection

hostel={"juice","bed","toilet"}
juice={"water","juice","apple"}
hermen=hostel.intersection(juice)
print(hermen)

sremen = {"apple","b","r","y"}
juice={"water","juice","apple"}
sremen.intersection_update(juice)
print(sremen)



gamer={"play","win","fail"}
ganster={"gamer","win","jermy"}
ress=gamer.difference(ganster)
print(ress)



set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.symmetric_difference(set2)
print(set3)