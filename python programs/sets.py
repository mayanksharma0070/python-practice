sets={3,2,4,6,2,"hello",True,False,True,0.1}
for item in sets:
    print(item)

cities={"tokyo","madrid","berlin","delhi"}
city2={"tokyo","seoul","kabul","madrid"}
city3=cities.union(city2)
cities.update(city2)
print(cities)
print(city3)

fruits1={"mango","grapes","pear","orange","banana"}
fruits2={"banana","guava","strawberry","watermelon","orange"}
fruits3=fruits1.intersection(fruits2)
print(fruits3)
fruits4=fruits1.union(fruits2)
print(fruits4)
fruits3.intersection_update(fruits4)
print(fruits3)

colours1={"red","pink","blue","orange","black"}
colours2={"yellow","green","white","pink","black"}
colours3=colours1.symmetric_difference(colours2)
print(colours3)
colours2.symmetric_difference_update(colours1)
print(colours2)

seher={"tokyo","berlin","delhi","london"}
seher2={"madrid","kabul","delhi"}
seher3=seher.difference(seher2)
print(seher3)
#similarly .difference_update()hello world hello world 