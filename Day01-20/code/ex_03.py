# """
# 每隔1秒输出一次“hello, world”，持续1小时
#
# Author: 骆昊
# Version: 1.0
# """
# import time
#
# for i in range(3600):
#     print('hello, world')
#     time.sleep(1)
from urllib.parse import uses_fragment

# """
# 每隔1秒输出一次“hello, world”，持续1小时
#
# Author: 骆昊
# Version: 1.1
# """
# import time
#
# for _ in range(3600):
#     print('hello, world',_)
#     time.sleep(1)

# """
# 从1到100的整数求和
#
# Version: 1.0
# Author: 骆昊
# """
# total = 0
# for _ in range(1, 101):
#     total += _
# print(total)

# """
# 从1到100的偶数求和
#
# Version: 1.0
# Author: 骆昊
# """
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(total)

# """
# 从1到100的偶数求和
#
# Version: 1.1
# Author: 骆昊
# """
# total = 0
# for i in range(0, 101, 2):
#     total += i
# print(total)

# """
# 从1到100的偶数求和
#
# Version: 1.2
# Author: 骆昊
# """
# print(sum(range(2, 101, 2)))

# """
# 从1到100的整数求和
#
# Version: 1.1
# Author: 骆昊
# """
# total = 0
# i = 1
# while i <= 100:
#     total += i
#     i += 1
# print(total)

# """
# 从1到100的偶数求和
#
# Version: 1.3
# Author: 骆昊
# """
# total = 0
# i = 2
# while i <= 100:
#     total += i
#     i += 2
# print(total)

# """
# 从1到100的偶数求和
#
# Version: 1.4
# Author: 骆昊
# """
# total = 0
# i = 2
# while True:
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total)

# """
# 从1到100的偶数求和
#
# Version: 1.5
# Author: 骆昊
# """
# total = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         continue
#     total += i
# print(total)

# """
# 打印乘法口诀表
#
# Version: 1.0
# Author: 骆昊
# """
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}×{j}={i * j}', end='\t')
#     print()

# """
# 输入一个大于1的正整数判断它是不是素数
#
# Version: 1.0
# Author: 骆昊
# """
# num = int(input('请输入一个正整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')

# """
# 输入两个正整数求它们的最大公约数
#
# Version: 1.1
# Author: 骆昊
# """
# x = int(input('x = '))
# y = int(input('y = '))
#
# # 确保 x <= y
# if x > y:
#     x, y = y, x
#
# while y != 0:
#     x, y = y, x % y
#
# print(f'最大公约数: {x}')

# """
# 猜数字小游戏
#
# Version: 1.0
# Author: 骆昊
# """
# import random
#
# answer = random.randrange(1, 101)
# counter = 0
# while True:
#     counter += 1
#     num = int(input('请输入: '))
#     if num < answer:
#         print('大一点.')
#     elif num > answer:
#         print('小一点.')
#     else:
#         print('猜对了.')
#         break
# print(f'你一共猜了{counter}次.')

# for num in range(0,100):
#     is_prime = True
#     for i in range(2, int(num ** 0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# a,b = 0,1
# for _ in range(20):
#     a, b = b, a+b
#     print(a)