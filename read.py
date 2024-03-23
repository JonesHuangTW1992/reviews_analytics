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

# 算留言平均長度
sum_len = 0 # 所有字串目前的總數
for d in data: # 每一筆資料命名為d
	sum_len += len(d) # sum_len = sum_len + len(d)
	# print(sum_len) = 顯示目前留言字數加總進度
print('平均留言長度是', sum_len/len(data), '個字')
# sum_len/len(data) = 留言總字數/留言總筆數 = 留言平均長度