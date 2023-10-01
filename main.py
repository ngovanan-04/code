# d1 = {'a':1, 'b': 2, 'c': 3}
# d2 = {'d': 100, 'e': 100, 'c': -100}
# d3 = {'a': 10, 'b': 4, 'c': 1000}
#
# res ={**d1, **d2, **d3}
from copy import deepcopy
numbers = [[2, [45, 65]], [24, 98]]
distore = {"an": 23, "uyen": 24, "anh": 22}
setbb = {2, 6, 7, 3}
sums = {2, 3, 5, 4, 8}
sumj = {20, 54, 80}

set3 = setbb.symmetric_difference(sums)
print(set3)
print(sums ^ setbb)
