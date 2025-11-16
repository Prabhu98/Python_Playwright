# A tuple is a sequence of values much like a list.
# The values stored in a tuple can be any type, and they are indexed by integers.
# The important difference is that tuples are #immutable.
# A tuple is created by placing all the items (elements) inside by parenthesis().
# Create Tuple
# Update Tuple
# Delete Tuple
# Slicing Tuple

# Way 1:
mobiles = ('sumsung', 'LG', 'OnePlus', 'Apple')

print(mobiles)
print(type(mobiles))

#Way 2:
#Create empty Tuple
mobiles = ()

print(mobiles)
print(type(mobiles))

#Way 3:
# Create single value Tuple - note possible in this way
mobiles = ('sumsung')
print(mobiles)
print(type(mobiles))

#Create single value Tuple
mobiles = ('sumsung', )
print(mobiles)
print(type(mobiles))


#Update

mobiles = ('sumsung', 'LG', 'OnePlus', 'Apple')
number = (1,2,3,4)

Order = mobiles + number
print(Order)

#Delete

# for Del - Note:: We cann't delete individual value in item
# del Order[1]

# can Delete entire Tuple only
del Order

# Slicing Tuple

mobiles = ('samsung', 'LG', 'OnePlus', 'Apple', 'OnePlus')
print(mobiles[0::])  # ['samsung', 'LG', 'OnePlus', 'Apple', 'OnePlus]

print(mobiles[::-1]) # ['OnePlus', 'Apple', 'OnePlus', 'LG', 'samsung']
print(mobiles[0:-2:2]) # ['samsung','OnePlus']
print(mobiles[0::3])  # ['samsung', 'OnePlus', 'OnePlus']

#mobiles[StartIndex:EndIndex:SkipIndex)

print(mobiles[::-2])  # ('Apple',OnePlus','LG','samsung')


#######################################################################

# Basic Operations - Tuples:-
# Tuple:-
# for length : len(tuple) : its return count of item
# for Concatenation : var_a + var_b : its concatenate 2 diff tuples (Note: new tuple output)
# for Repetation : tuple_var_a*2 : its printed tuple twice
# for membership : in / not in : its return True or False(based on Condition)
# for Iterative : for loop : its returns each item in the tuple
# for maximum : max(tuple) : its will return maximum item in the tuple
# for minimum : min(tuple) : its will return minium item in the tuple
# for index : tuple_var.index(ele) : its will return item position in the tuple
# for count : tuple_var.count(ele) : its will return element count in the tuple
# for String to tuple : tuple('test') : output -> ('t', 'e', 's', 't')
# for list to tuple : tuple(list) : output -> (tuple output)

##########################################################################

# Count of Tuples

mobiles2 = ('samsung', 'LG', 'OnePlus')
len(mobiles2)

# Concatenate of Tuples

mobiles = ('sumsung', 'LG', 'OnePlus')
items = (1,2,3)

m_item = mobiles + items
print(m_item)


# Repetations
print(mobiles * 2)

# Membership
mobiles = ('sumsung', 'LG', 'OnePlus')

print('LG' in mobiles)
print('iphone' in mobiles)

print('-----------------------------')

print('iphone' not in mobiles)
print('LG' not in mobiles)

#maximum - minimum

print('Maximum item ::', max(mobiles))
print('Minimum item ::', min(mobiles))

#element index item number

mobiles = ('sumsung', 'LG', 'OnePlus')
print(mobiles.index('LG'))

#Convert List into Tuple

# Str to Tuple
a = 'Testleaf'
print(tuple(a))

print('----------------------------------------')

# List to Tuple
b = ['a', 'b', 'c', 'd']
print(tuple(b))

z = tuple(b)

