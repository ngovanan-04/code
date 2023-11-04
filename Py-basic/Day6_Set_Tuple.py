"""
+ Set
+ Tuple

"""

# Tuple

tup1 = 1, 2 , 3 
tup2 = (3, 4, 5)
tup3 = 6, 
tup4 = (7,)

# Truy cập giá trị tuple : print(variable[index])
print(tup1[1])

# Thêm giá trị vào tuple : variable += (7, 8, 9)
tup1 += (4, 5, 6)
print(tup1)



# Set (set có giá trị không thự tự và các giá trị không trùng lặp)

# tạo một set trống
set1 = set()

# Thêm một giá trị vào set : variable.add(value)
set1.add(2)

# cập nhập giá trị mới trong set: variable.update([value, value, ...])
set1.update([3, 5 , 7 ,9])
print(set1)

# xóa giá trị trong set : variable.remove(value)
set1.remove(7)
print(set1)

# Sao chép set : new_set = old_set.copy()
set2 = set1.copy()
print(set2)

# Làm trống set : variable.clear()
set2.clear()
print(set2)


# Tạo set :
set3 = {4, 6, 7 , 8, 2}

# Thêm chuổi vào set (list không thể thêm vào set) :
set3.add("an")
print(set3)

# Lấy giá trị bất kỳ và trả về giá trị đó : variable = set1.pop()
any_value = set3.pop()
print(any_value)


# Hàm kiểm tra giá trị và kiểu => trả về bool
print(isinstance(3, int))

# Hàm trả về mã ascci :
print(ord('a'))

# Hàm in ra dấu  'value' :
s = 't'
print(repr('b'))
print(f"{s!r}")