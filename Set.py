##########################################################

# Learn_Set
#
# A Set is unordered collection of Elements or Items
#
# Its doesn't allows the duplicate values which means it allows only unique values.
#
# A set is created by placing all the items (elements) inside curly braces {}.
#
# We cannot access or change an element of set using indexing or slicing.(because of unorder)
#
# Set
# add : its add values in existing set(one element).
#
# update : its add multiple values like list with set.
#
# remove : its remove the value bases on given value. remove is not work based on indexing(because of unorder).
#
# discard : its remove the value bases on given value.
#
# pop : its remove the element of the set.
#
# clear : its clear entire set.
#
# len : its return count of item in the set.
#
# sum : sum the each item in the set(only for integer).
#
# min : its print minimum value in the given list.
#
# max : its return maximum value in the given list.

###########################################################

s = {'a'}
print(type(s))

a_version = {"Pie", "Oreo", "Nougat", "Marshmallow"}
print(a_version)
print(type(a_version))

print("--------------------------------------------")


a_version = {}
print(a_version)
print(type(a_version))

print("--------------------------------------------")

a_version = {"Jelly Bean"}
print(a_version)
print(type(a_version))


##############

# Add the item into set.

a_version.add("Pie")
a_version.add("Oreo")
a_version.add("Nougat")
a_version.add("Marshmallow")
print(a_version)

# print(a_version.remove('11111'))

#Update the item into set

a_version = {"Pie", "Oreo", "Nougat", "Marshmallow"}
b_version = {"Lollipop", "KitKat", "Jelly Bean", "Lollipop"}
a_version.update(b_version)
print(a_version)

#Set -> not support indexing

# print(a_version[2])

#remove item based on value using remove - not an index

a_version = {"Pie", "Oreo", "Nougat", "Marshmallow"}
a_version.remove("Oreo")
print(a_version)

#using Pop fun
a_version = {"Pie", "Oreo", "Nougat", "Marshmallow"}
a_version.pop()
print(a_version)

#add new item in the Set

a_version.add("Lollipop")
print(a_version)