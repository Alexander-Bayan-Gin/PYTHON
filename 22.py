my_list = []
my_list.append(list(map(int,input().split())))
n = len(my_list[0])
k = 1
while k < n:
    my_list.append(list(map(int,input().split())))
    k += 1

res = sum(my_list[0])

if all([sum(x) == res for x in my_list]) and all([sum(x) == res for x in list(zip(*my_list))]):
    print('YES')
else:
    print('NO')