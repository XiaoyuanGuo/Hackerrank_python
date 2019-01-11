from collections import OrderedDict
n = int(input())
d = OrderedDict() 
for i in range(n):
    item, space, price = input().rpartition(' ')
    d[item] = d.get(item,0) + int(price) 
for i , q in d.items():
    print(i, q)
