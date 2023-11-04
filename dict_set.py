
#Viết chương trình cập nhật thông tin và điểm số của sinh viên

dicti = {'an': 4, 'nhat':6, 'hien': 7}
old_dict = {}

if dict != old_dict:
    dict.update({'an': 3, 'hien': 9})
    print(" \nĐã cập nhật điểm số của SV an, hien \n")

def nhap():
    print("luu y nhap day du cac cap: <key>-<value> cach nhau bang ' '")
    list_key = input('Nhap key: ').lstrip().split()
    list_value = input('Nhap value: ').lstrip().split()

    kq = dict(zip(list_key, list_value))
    return kq

if len(old_dict) == 0:
        old_dict = nhap()
        print('\nĐã tạo mới một ds sinh viên và điểm số!\n')

print('Sau khi tao ds SV:')
print(old_dict)
print('\nSau khi duoc cap nhat ds SV:')
print(dicti)


# Viết chương trình tính điểm trung bình của các học sinh

D = {'An ': [7, 9], 'Binh': [10, 8.5], 'Cuong': [9, 8], 'Dung': [8, 8], 'Duc': [9.5, 7]}

print('\nDIEM TRUNG BINH: \n')
for Name,Gpa in D.items():
    if Gpa != 0:
        tong = sum(Gpa)
        DTB = tong / 2
        print(f"{Name} \t {DTB}")


# Viết chương trình tạo tập hợp A

a = set()
from random import random

for i in range(5):
    a.add(int(10 * random()))
print('\nSau khi tao 5 so ngau nhien:')
print(a)


# Viết chương trình tách B thành 2 tập con M và N:

B = {'an', 'ngu', 'hoc', 25, 43, 3.14}
M = set()
N = set()

for i in B:
    if isinstance(i, str):
        N.add(i)
    else:
        M.add(i)

print('\nSau khi tach thanh hai tap con:\n')
print('Tap M chua ky tu so: ',M)

print('Tap N chua xau ky tu : ',N)


# Viết chương trình sinh ngẫu nhiên 2 tập C và D

C = set()
D = set()

for i in range(10):
    C.add(int(10*random()))
    D.add(int(10*random()))

print('\nSinh ngau nhien tap C: ',C)
print('Sinh ngau nhien tap D: ',D)
print('\nCac ptu chung cua C va D: ', C.intersection(D))
print('Cac ptu thuoc C ma khong thuoc D: ', C.difference(D))
print('Cac ptu thuoc D ma khong thuoc C hoac nguoc lai: ', D.symmetric_difference(C))
