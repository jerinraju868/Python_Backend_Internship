''' Swap two tuples in Python​
    tuple1 = (11, 22)
    tuple2 = (99, 88)
'''

# tuple inputs
tuple1 = (11,22)
tuple2 = (99,88)

# displaying the tuples before swapping
print('Before Swaping : ', tuple1, tuple2)

# swapping the tuples
tuple1, tuple2 = tuple2, tuple1

# displaying the tuples after swapping
print('After Swapping : ', tuple1, tuple2)