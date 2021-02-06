import numpy

integers = input().split(" ")

for i in range(0, len(integers)):
    integers[i] = int(integers[i])

change_array = numpy.array(integers)
change_array.shape = (3,3)
print(change_array)
