# height = float(input("身高(cm):"))
# weight = float(input("体重(kg):"))
# bmi = weight / (height / 100) ** 2
# print(f'{bmi = :.1f}')
# # if 18.5 <= bmi < 24:
# #     print('你的身材很棒！')
# # else:
# #     print('你的身材不够标准哟！')
# if bmi < 18.5:
#     print('你的体重过轻')
# elif bmi < 24:
#     print('你的身材很棒')
# elif bmi < 27:
#     print('你的体重过重！')
# elif bmi < 30:
#     print('你已经轻度肥胖！')
# elif bmi < 35:
#     print('你已经中度肥胖！')
# else:
#     print('你已经重度肥胖！')


# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400: description = 'Bad Request'
#     case 401: description = 'Unauthorized'
#     case 403: description = 'Forbidden'
#     case 404: description = 'Not Found'
#     case 405: description = 'Method Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)


# status_code = int(input('响应状态码: '))
# match status_code:
#     case 400 | 405: description = 'Invalid Request'
#     case 401 | 403 | 404: description = 'Not Allowed'
#     case 418: description = 'I am a teapot'
#     case 429: description = 'Too many requests'
#     case _: description = 'Unknown Status Code'
# print('状态码描述:', description)

# x = int(input('输入x：'))
# if x>1:
#     y = 3*x - 5
# elif -1<=x<=1:
#     y = x+2
# else:
#     y = 5*x+3
# print(f'{y=:}')

# """
# 百分制成绩转换为等级制成绩
#
# Version: 1.0
# Author: 骆昊
# """
# score = float(input('请输入成绩: '))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print(f'{grade = }')

# """
# 计算三角形的周长和面积
#
# Version: 1.0
# Author: 骆昊
# """
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     perimeter = a + b + c
#     print(f'周长: {perimeter}')
#     s = perimeter / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     print(f'面积: {area}')
# else:
#     print('不能构成三角形')