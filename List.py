# Create List

mobiles = ['samsung', 'LG', 'OnePlus', 'Apple', "sample"]
print(mobiles)


#Index

print("Value of 0th Index" ,mobiles[0])
print(type(mobiles))
print(min(mobiles), max(mobiles))
print(len(mobiles))

#Reverse by using slicing

print(mobiles[::-1])

#Methods in List

# append() - append at the end of the list
mobiles.append("Iphone")
print(mobiles)
# extend() - add list of element in the list
mobiles.extend(["Oppo","Dell","HP"])
print(mobiles)

# Another way to extend the list of values
mobiles = mobiles + ["Honor", "Sony", "Gopi"]     # or   mobile += ["Honor", "Sony"]
print(mobiles)

# insert value based on specific index number
mobiles.insert(2, "Gopi")
print(mobiles)

#Remove  - if two value in the list, it will remove the first occurance
mobiles.remove('Gopi')
print(mobiles)

# for revered - using loop
mobile =  ['Balaji','Loges','Sriram','Alok']

for item in reversed(mobile):
    print(item)

number = [10,30,20,89]

for result in reversed(number):
    print(result)


# Sorted - using loop

sports = ['Cricket','Football','Soccer','Wrestling','Tennis','Badminton']
for sport in sorted(sports):
    print(sport)

Value = sports.copy()
print("New Value" , Value)


#Reverse

sports.reverse()
print(sports)

#Sort
sports.sort()
print(sports)


#count - Occurrence
print(sports.count('Soccer'))



# Pop - Remove last element and return the value

sports.pop()
print(sports)

# Remove with Index value

sports.remove('Tennis')
print(sports)

sports.pop(0)
print(sports)

sports.clear()
print(sports)

