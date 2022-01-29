dic = input().lower().split()
new_dic = {}
for k in dic:
    if k in new_dic:
        new_dic[k] += 1
    else:
        new_dic[k] = 1
for n in new_dic:
    print(n, str(new_dic[n]))
-----------------------------
dic = input().lower().split()
new_dic = {k: dic.count(k) for k in dic}

for key, value in new_dic.items():
    print(key, str(value))
