# d1 = {'a':1, 'b': 2, 'c': 3}
# d2 = {'d': 100, 'e': 100, 'c': -100}
# d3 = {'a': 10, 'b': 4, 'c': 1000}
#
# res ={**d1, **d2, **d3}
# from copy import deepcopy

# Cho chuỗi ký tự: s = “ngay-14-thang-10-nam-2023”.

s = "ngay-14-thang-10-nam-2023"
A = []
temp = ''
for i in s:
    if i.isdigit():
        temp += i
    elif temp != '':
        A.append(int(temp))
        temp = ''
if temp != '':
    A.append(int(temp))

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in A:
    if ngto(i):
        print(i)


# Nhập vào một chuỗi ký tự S gồm chữ cái và chữ số.

s = str(input("nhap chuoi ky tu: "))
cout_str = 0
cout_int = 0

for char in s:
    if char.isalpha(): #isalpha() tra ve True neu la chu cai và nguoc lai
        cout_str += 1
print("chieu dai cua ky tu co trong chuoi: ",cout_str)

for int in s:
    if int.isdigit(): #isdigit() tra ve True neu la chu so và nguoc lai
       cout_int += 1
print("chieu dai cua chu so co trong chuoi: ",cout_int)


#Nhập vào hai chuỗi ký tự S1 và S2. Viết đoạn chương trình:

s1 = str(input('Nhap chuoi S1: '))
s2 = str(input('Nhap chuoi S2: '))

def ktr(s1, s2):
    cout = 0
    if s2 in s1:
        print("\ns2 la chuoi con cua s1!")
        for i in s1:
            if s2 in i:
                cout += 1
        print('So lan xuat hien cua chuoi s2: ', cout)
    else:
        print("\ns2 khong phai la chuoi con cua s1!")

a = ktr(s1,s2)
print(a)


# Nhập từ bàn phím họ tên của bạn.

Ten = input('Nhap ho va ten: ')
Name = Ten.split()

hoten = Name[0] + ' ' + Name[-1]

def ktr_dem(Name):
    tmp = ''
    for i in Name:
        if i != Name[0]:
            if i != Name[-1]:
                tmp += i
                tmp += ' '
    return tmp

print('chuoi sau khi dao nguoc: ',Ten[::-1])
print(f'ho ten: {hoten}, chu dem: {ktr_dem(Name)}')


#Viết hàm Component(s,k)
def component(s,k):
    if k > len(s):
        return False
    else:
       return s[k-1]

s = "I hate python"

print(component(s,4))
print(component(s,7))
print(component(s,10))
print(component(s,15))
