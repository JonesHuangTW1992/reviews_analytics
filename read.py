data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line) # 把line 加進去 data裡面
# print(len(data)) = 每讀一行就把長度顯示出來(讀取進度)		
# print(len(data)) = 顯示總共有幾筆留言
# print(data) = 顯示所有留言
# print(data[0]) = 顯示第0筆留言
		count += 1 # count = count + 1
		if count % 1000 == 0: # 若是1000的倍數
			# % = 求餘數
			print(len(data)) #才顯示讀取進度
print('檔案讀取完成, 總共有', len(data), '筆留言')
