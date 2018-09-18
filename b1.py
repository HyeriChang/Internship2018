x=int(input("Nhap mot so:"))
with open('data.txt') as f:
	count = 0
	for noi_dung in f:
		count +=1
		if count == x:
			print(noi_dung)
"""
chươnng trình nhập 1 số x vào, lấy dòng thứ x trong file đó ra

"""