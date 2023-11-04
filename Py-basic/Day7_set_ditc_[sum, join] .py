"""
    + Advanced set
    + Dictionaty
    + sum, len, min, max, join
"""


# Set:

set1 = {2, 5, 7, 9, 6, 4}
set2 = {1, 3, 4, 6, 8,}


# Tìm ptử chung (phép giao) của hai set:   set3 = set1.intersection(set2)     or    print(set1 & set2)
set3 = set1.intersection(set2)
print(set3)

# Tìm ptử của set1 mà set2 không có:   set3 = set1.difference(set2)     or    print(set1 - set2)
set3 = set1.difference(set2)
print(set3)

# Láy các ptử của hai set vào set mới (phép hợp):   set3 = set1.union(set2)     or    print(set1 | set2)
# Thực hiện với nhiều set:  set =set1.union(set2).union(set3)      or   print(set1 | set2 | set3)    
set3 = set1.union(set2)
print(set3)

# Lấy các ptử của hai set nhưng trừ đi phần chung (phép trừ đối xứng): set3 = set1.symetric_difference(set2)  or print(set1 ^ set2)
set3 = set1.symmetric_difference(set2)
print(set3)




# Dict:

student = {"name": 'An', "age": 20, "grades": [45, 60, 74, 88]}

print(student)

# In ra dict đẹp hơn
import json

print(json.dumps(student, indent=4)) 
# Để biến một dict thành một chuổi       ||      indent=4 : thụt lề(spaces) bằng 4

# In ra value của key: value = studen.get("key1", 'sv001')    // trả về giá trị của key trong dict or giá trị mặc định nào đó      
value = student.get("name")
value1 = student.get("id", "shi")     
print(value)

# Thêm một cặp key value vào dict:  student ["key"] = "SV001"
student ["id"] = "SV001"

# Cập nhật thêm vào dict (tuole, new_dict):   student.update(key1 = "value", key2 = "value")

# student.update(id = "SV001")
# tuple:
info = [
    {"id", "SV001"},
   { "gender", "male"}
]
#new_dict:
info1 = {
    "id": "SV001",
    "gender": "male"
}
student.update(info1)
print(student)

#remove
valuee = student.pop("name")
del student["id"]
print(valuee)

# Xóa đi cặp key value cuối và trả về cặp đó: tup = student.popitem()
tup = student.popitem()
print(tup)


# Lấy key, value or tất cả các key value thành list: item = list(student.items())
keys = list(student)
values = list(student.values())
items = list(student.items())
print(items)

# Làm trống dict:   student.clear()
student.clear()
print(student)




# sum:

ist = [1, 2, 3, 4]

# Truyền tham sô vào hàm sum thay tham số mặc định là 0 (để trống): total = sum(ist, 10)
total = sum(ist, 10)
print(total)

imp = [[2, 6, 8, 4], [5, 7, 9, 1]]

# list cộng với list: 
ind = sum(imp, [0])
print(ind)


# len:

api = ['a', 'n', 's', 'h', 'i']
print(len(api))


# min, max:

inte = [2, 6, 9, 7, 3]
print(min(inte))
print(max(inte))


# join:

mra = [3, 5, 7, 9]

# chuyển một list thành chuổi   // comvert một list số thành chuổi
s = ' '.join(map(str, mra))

print(s)



