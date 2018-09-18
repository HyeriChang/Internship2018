with open('config.txt', 'r') as file:
    x = file.readlines()
    num = ''.join(x) #list sang string
    num=int(num)			# string sang int
   #print(num)
with open('data.txt') as f:
	count = 0
	for noi_dung in f:
		count +=1
		if count == num:
			print(noi_dung)
"""
Cho file config.txt chứa 1 số x trong khoảng từ 1- 100
file data.txt có 100 line 
in nd dong thu x trong file data ra ngoai man hinh
"""