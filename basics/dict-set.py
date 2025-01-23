#sets {}
# a={1,2,3,4,6,4,1}
# print(a[0])#cant access elemt using indexing
#unordered , unindexed, no duplicate 
#faster than list to check data is present
utensils={"spoon","fork","knife"}
dishes={"bowl","plate","cup","knife"}
utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)
dinner_table=utensils.union(dishes)
print(utensils.difference(dishes)) #what is different 
print(utensils.intersection(dishes))

for x in dinner_table :
    print(x)

#dictionary : key value pair stored ,{}
#changable , unordered, fast as they use hashing allowing to access values
capitals={'USA':'washington dc',
          'india':'new delhi',
          'china':'beigin',
          'russia':'mascow'}
capitals.update({'germeny':'berlin'})
capitals.update({'usa':'las vegas'})
capitals.pop('china')
capitals.clear()
#print(capitals['russia'])
print(capitals.get('Germany')) #return none but not an KeyError
print(capitals.keys())
print(capitals.values())
print(capitals.items())


for key,value in capitals.items():
    print(key,value)   #entire dictionary 






marks={'kch':34, 'pch':45,'Nitu':68,22:44}
print(marks[22])

squares={1:1,3:9,5:25,7:49,9:81}

