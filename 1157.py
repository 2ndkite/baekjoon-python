w = input().upper()
w_list = list(set(w)) 
cnt_list = []

for i in w_list:
    cnt = w.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
else:
    print(w_list[(cnt_list.index(max(cnt_list)))])
