ramwalk=("kos","froxi","kwna")
print(ramwalk)

ramwalk=("his","urekka","wertyy")
print(len(ramwalk))


rosamma=("gym")
print(type(rosamma))

x =("apple","banan","grapes")
y=list(x)
y[1]="dragon"
x=tuple(y)
print(x)

raju=("men","women","press")
transun=list(raju)
transun[1]="wallet"
raju=tuple(transun)
print(raju)


ganga=("kiss","herly","sally")
menly=list(ganga)
menly.append("griss")
ganga=tuple(menly)
print(ganga)

herman=("newgen","jacob","keernal")
armaqqn=("gangster", )
herman += armaqqn
print(herman)


dasler=("radio","makeup","delivery")
host=list(dasler)
host.remove("delivery")
dasler=tuple(host)
print(dasler)

circus=("kollam","pathanamthitta","kottayam")
print(circus)

kedra=("hell","donn","saas")
(green,yellow,james)=kedra
print(green)
print(yellow)
print(james)

filmfestival=("actors","directors","musicals","angors")
(green,yellow,*red)= filmfestival
print(green)
print(yellow)
print(red)

filmfestivals=("actors","directors","musicals","anchors","actors","musicals","anchors")
print("The original tuple is : " + str(filmfestivals))
res = tuple(set(filmfestivals))
print("The tuple after removing duplicates : " + str(res))

#loop tuuples

ganster=("gamer","jorgert","konik","jermy")
for x in ganster:
    print(x)


farmer=("agriculture","farm","crops","machines")
for i in range(len(farmer)):
    print(farmer[i])

ganga=("kiss","herlly","sally","roshan")
i=0
while i<len(ganga):
    print(ganga[i])
    i=i+1


#join tuples

raju=("men","women","press")
ramwalk=("his","urekka","wertyy")
lootpaisa=ramwalk+raju
print(lootpaisa)


school=["teacher","mysore","jaipur","kanpur","goa","punjab","kanpur"]
travker = school*3
print(travker)


