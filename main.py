# d1 = {'a':1, 'b': 2, 'c': 3}
# d2 = {'d': 100, 'e': 100, 'c': -100}
# d3 = {'a': 10, 'b': 4, 'c': 1000}
#
# res ={**d1, **d2, **d3}
# from copy import deepcopy

s = "ngay-14-thang-10-nam-2023"
import re
A = re.findall(r'\d+', s)

print(A)
# for i in a:
#     int(a)
#     if(a[i] - i == 0):
#         print(i)
