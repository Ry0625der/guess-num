#讓使用者決定隨機整數範圍
#讓使用者重複輸入數字去猜
#猜對的話 印出"恭喜答對了"
#猜錯的話 要告訴他 比答案大/小
#過程中要印出" 這次猜第幾次

import random
start = input('請先決定隨機數字範圍開始值: ')
end = input('再決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count +1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜答對了!')
		print('這次猜第', count, '次')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('這是猜第', count, '次')

