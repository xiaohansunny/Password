password = 'a123456'
x = 3
while True:
	pin = input('请输入密码: ')
	if pin == 'password':
		print('登录成功!')
		break
	else:
		x = x - 1
		print('密码错误，还有',x,'次机会')
		if x == 0:
			break