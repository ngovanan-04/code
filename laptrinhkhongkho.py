firts_name = 'An'
last_name = 'Uyen'
full_name = firts_name + ' ' + last_name
print('Wendding: ' + full_name)

#doc
vi=open('project.inp')
# doc hnag va cot
n=vi.readline().split()
h,c=int(n[0]), int(n[1])
# doc list 2 chieu
y=[]
for i in range(h):
    a=list(map(int,vi.readline().split()))
    y.append(a)
# a=list(map(int,a))

# ghi
bon=open("project.out",'w')
bon.write(f'{y}')

print("pretty {}".format(full_name))