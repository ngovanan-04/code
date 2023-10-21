"""
+ list

"""

from copy import deepcopy
numbers = [2, 3, 5, 7, 9]


# truy cập vị trí giá trị của list:  0 1 2 . . . -3 -2 -1
print(numbers[0])

# thêm giá trị ở cuối list:  numbers.append(value)
numbers.append(10)
print(numbers)

# xóa một giá trị trong list:  numbers.remove(value)  or del numbers[value]
numbers.remove(5)
print(numbers)
del numbers[2]
print(numbers)

# xóa giá trị cuối và trả về giá trị đó:  last_value = numbers.pop()
last_value = numbers.pop()
print(last_value)

# thêm một list mới vào list cũ:  numbers.extend([24, 30, 50, 62, 80, 90, 100])
numbers.extend([24, 30, 50, 62, 80, 90, 100])
print(numbers)

# thay đổi một giá trị ở trong list:  numbers[location] = value
numbers[0] = 12
print(numbers)

# trả về số lần xuất hiện của giá trị:  variable = numbers.count(value)
amount = numbers.count(3)
print(amount)

# làm trống list: numbers.clear()
numbers.clear()
print(numbers)

# trả về đồ dài của list:  amounti = len(number)
amounti = len(numbers)
print(amounti)

# chèn giá trị vào một vị trí bất kỳ(đầu: 'n-1', cuối: 'n+1' hoặc vị trí có trong list) ở trong list:  numbers.insert(location, value)
numbers.insert(0, 20)
print(numbers)

# trả về vị trí của giá trị có trong list:  variable = numbers.index(value)
index_of_value = numbers.index(20)
print(index_of_value)

# đảo ngược lại vị trí của list:  numbers.reverse()
numbers.reverse()
print(numbers)

# sắp xếp các giá trị tăng dần có trong list:  numbers.sort()
# sắp xếp các giá trị giảm dần có trong list:  numbers.sort(reverse=True)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# tìm giá trị lớn nhất và nhỏ nhất trong list:  variable = max(numbers)  || variable = min(numbers)
max_value = max(numbers)
min_value = min(numbers)
print(max_value)
print(min_value)


"""   Day-5

+ list in list
+ copy list
+ list slicing => new list

"""

# list trong list : variable = [[value, value, ...], [value, value, ...], ...]

friends = [["ngo", 22], ["van", 10], ["an", 20006]]

# lấy list con trong list : print(variable[index][index]...)
print(friends[0][1])

# copy list : variable2 = variable1.copy()
list_copy = friends.copy()
print(list_copy)

# lấy giá trị từ trong list sang list mới : new_list = old list[start:stop:step]
# bản sao list slicing : variable = list[:]  /  đảo ngược: variable = list[::-1]
new_list = friends[0:2:1]
print(friends is new_list)     # so sánh địa chỉ
print(new_list)

# Copy list nhưng không bị ảnh hưởng do có thao tác thêm hoặc xóa trước đó (copy list gốc)


lst = [[1, [2, 3]], (5, 6)]
lst1 = deepcopy(lst)

lst[0][1].append(10)

print(lst1)
