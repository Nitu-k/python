#list store multiple item i single variable
#mutable data type
food=["pizza","burger","noodles"]
food[0]="sushi"
print(food[0])

#function of list
food.append("ice cream")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:# prints all the element togeather
    print(x)



#2D LIST: multi d list , list of seperate list
drinks=["coffee","soda","tea"]
dinner=["pizza","burger"]
desert=["cake","icecream"]

fooditem=[drinks, dinner, desert]
print(fooditem[0][0])#indexing multilist we acces a particular list



my_list=[1,2,3,"Nitu"]
print(my_list)

fruit=["Apple","Guava","Papaya"]
fruit[1]='Mango'
print(fruit[0])
print(fruit)

numbers=[0,1,2,3,4,5]
print(numbers[::-1])

#list comprehension
a=[0,1,2,3,4,5,6,7,8,9]
print(a)
#or
a=[x for x in range (10) if x%2==0]
print(a)

b=[3**i for i in range (10)]
print(b)

#adding value to a list by appending the list
a=[6,5,7,1,2,3]
fruits=['Banana','apple','kiwi']
print(fruits.index('apple'))
print(fruits.count('kiwi'))
a.sort()
#a.append(4)
print(a)

#list function (without dot )
#len, max, min, list(seq), sum(list)
g=[6,3,2,4,7,8,9,1]
print(len(g))
print(max(g))
print(min(g))
print(sum(g))
s="nitu"
print(list(s))





